# 天気Bot

LineNotifyで天気を通知してくれるBOTです。

## 各自で指定すること

入力項目は**3つ**あり、各自で任意の**トークン・都市・通知時間**を入れれば誰でも使えるようになると思います。**トークン発行は必須です**

- **アクセストークンの発行**でお世話になったサイト様  

[Lineのアクセストークン発行方法](https://qiita.com/pontyo4/items/10aa0ba0a17aee19e88e)

- **都市名**はこの中にあるものをお使いください

  - [全国の地点定義表](https://weather.tsukumijima.net/primary_area.xml)

- **通知時間**は「HH:MM」の形式（例：09:30）

  - おすすめは **00:00 ~ 06:59** です。（気象庁の情報が朝7時に切り替わり、最低気温の情報がなくなるため）
  
## ファイルの自動起動について

私の環境ではRaspberry Piで実行していますが、再起動をしても自動的にファイルが起動するようにしました。
少し手間取ったため一応ここに記載します



## コード作成において大変参考にしたサイト様
* [LineBotの作り方（python）](https://datadriven-rnd.com/linebot/)
* [Python で 天気予報APIからお天気情報を取得してみよう](https://kenkyujinsei.com/2021/02/06/python-%e3%81%a7-%e5%a4%a9%e6%b0%97%e4%ba%88%e5%a0%b1api%e3%81%8b%e3%82%89%e3%81%8a%e5%a4%a9%e6%b0%97%e6%83%85%e5%a0%b1%e3%82%92%e5%8f%96%e5%be%97%e3%81%97%e3%81%a6%e3%81%bf%e3%82%88%e3%81%86/)
* [Scheduleモジュールを用いたイベント定期実行](https://di-acc2.com/programming/python/4574/)

### 天気APIの使用元
* [天気予報 API（livedoor 天気互換）](https://weather.tsukumijima.net/)
