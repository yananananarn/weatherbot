import requests
import xml.etree.ElementTree as ET
import os
import datetime
import schedule
from time import sleep

# Enter any value by each user
line_notify_token = "your-token"
city_name = 'さいたま'
notice_time = '07:00'

def main():
    schedule.every().days.at(notice_time).do(getWeather)
    # schedule.every(10).seconds.do(getWeather)
    while True:
        schedule.run_pending()
        sleep(1)
    

def lineSend(message):
    #bot settings
    url = "https://notify-api.line.me/api/notify"
    
    message = '\n' + str(message)

    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    # message send
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
    
    today_weather = city_name + 'の' + json_file['forecasts'][0]['dateLabel'] + 'の天気は, ' + json_file['forecasts'][0]['telop'] + 'です．'
    description = json_file['description']['text']

    print(json_file)

    # Send to Line
    lineSend(today_weather)
    lineSend(description)
    lineSend('予報日 ' + json_file['forecasts'][0]['date'])
    
    
if __name__ == "__main__":
    main()
