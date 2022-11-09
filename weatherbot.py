import requests
import xml.etree.ElementTree as ET
import os
import datetime
import schedule
from time import sleep

# Enter any value by each user
line_notify_token = "your-token"
city_name = 'さいたま'
notice_time = '06:50'

def main():
    lineSend("起動しました\n" + str(datetime.datetime.now().replace(microsecond=0)))
    getWeather()

    schedule.every().days.at(notice_time).do(getWeather)
    # schedule.every(10).seconds.do(getWeather)
    while True:
        schedule.run_pending()
        sleep(1)
    

def lineSend(message):
    url = "https://notify-api.line.me/api/notify"
    
    message = '\n' + str(message)

    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    # メッセージを送信
    requests.post(url, data=payload, headers=headers)


def getWeather():
    xml_url = 'https://weather.tsukumijima.net/primary_area.xml'
    base_url ='https://weather.tsukumijima.net/api/forecast/'

    xml_file = requests.get(xml_url).text
    root = ET.fromstring(xml_file)
    city_id_dict={}
    for value in root.iter('city'):
        city_id_dict[value.attrib['title']] = value.attrib['id']
        
    json_file = requests.get(os.path.join(base_url,'city',city_id_dict[city_name])).json()

    if datetime.time(12, 0, 0) <= datetime.datetime.now().time() <= datetime.time(23, 59, 59):
        forecast_day = 1
    else:
        forecast_day = 0
    
    # jsonファイルから変数に格納
    title = json_file['forecasts'][forecast_day]['date'] + 'の' + city_name
    telop = '・天気\n' + json_file['forecasts'][forecast_day]['telop']
    tem_min = json_file['forecasts'][forecast_day]['temperature']['min']['celsius']
    tem_max = json_file['forecasts'][forecast_day]['temperature']['max']['celsius']
    temp = '・気温\n 最高      最低\n'+ str(tem_max) + '℃      ' + str(tem_min) + '℃'

    # 降水確率を配列に格納
    chance_of_rain = []
    cor_text = "・降水確率\n 0  -   6  -  12  -  18  -  24\n   "
    for i in range(4):
        chance_of_rain += [json_file['forecasts'][forecast_day]['chanceOfRain']['T'+f'{i*6:02}'+'_'+f'{(i+1)*6:02}']]
        cor_text += chance_of_rain[i] + '    '

    # 送信メッセージに入れる
    sendMessage = '\n' + title + '\n\n' + telop + '\n\n' + temp + '\n\n' + cor_text

    # Send to Line
    lineSend(sendMessage)
    

if __name__ == "__main__":
    main()
