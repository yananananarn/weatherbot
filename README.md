# 天気Bot

LineNotifyで天気を通知してくれるBOTです。

<img width="500" src="https://assets.st-note.com/production/uploads/images/90830879/picture_pc_ec653c6f817261bf2fe821f30571f5f3.png?width=800">

## 各自で指定すること

入力項目は**3つ**あり、各自で任意の**トークン・都市・通知時間**を入れれば誰でも使えるようになると思います。**トークン発行は必須です**

- **アクセストークンの発行**でお世話になったサイト様  

  - [Lineのアクセストークン発行方法](https://qiita.com/pontyo4/items/10aa0ba0a17aee19e88e)

- **都市名**はこの中にあるものをお使いください

  - [全国の地点定義表](https://weather.tsukumijima.net/primary_area.xml)

- **通知時間**は「HH:MM」の形式（例：09:30）

  - おすすめは **00:00 ~ 04:59** です。（気象庁の情報が朝5時に切り替わり、最低気温の情報がなくなるため）
  
## ファイルの自動起動について

私の環境ではRaspberry Piで実行していますが、再起動をしても自動的にファイルが起動するようにしました。

少し手間取ったため一応ここに記載します。いくつか方法はあるらしいですが、**systemd**を使いました。
Linuxでもできると思います。

### 手順

1. 自動起動の設定ファイルを作るため、まず`cd /etc/systemd/system`で適切な場所に移動する

2. 次にファイルを作る。`sudo nano [サービス名].service`でファイルを作り、編集する。  
[サービス名]は任意の名前。今回は`weatherbot.service`にしている

3. 設定の詳細を記述する。{ }この括弧があるところは各自の環境で修正してください。( { }この括弧はいらない )


```service:/etc/systemd/system/weather.service
[Unit]
Description={ 任意の説明文(例：Do weatherbot) }
After=network-online.target
ConditionPathExists={ 実行ファイルがおいてあるディレクトリのパス(例：/home/pi/desktop) }

[Service]
ExecStart=/usr/bin/python3 { 実行ファイルのパス(例：/home/pi/desktop/weatherbot.py) }
Restart=always
RestartSec=10
Type=simple

[Install]
WantedBy=multi-user.target
```


4. 入力できたら`Ctrl + O`で保存、`Ctrl + X`でエディタを抜ける。

5. 作成した設定ファイルを`sudo systemctl start [サービス名].service`でサービスを開始。  
正しく起動しているかどうかは`sudo systemctl status [サービス名].service`にて確認できる

6. まだこの状態だと電源を落とすと止まってしまうため、`sudo systemctl enable [サービス名].service`を打つ。
そうすることで機器を起動した際に自動起動ができるようになる。

7. 後は再起動をしてきちんと自動実行ができているかどうか確認する

### もし`ImportError: No module named schedule`のようなエラーが出たとき
上記のエラーが出たときは、scheduleモジュールがきちんとインストールされていないときです。  
恐らく普通に実行する際は問題ないのですが、systemdで実行しているとユーザーディレクトリにモジュールをインストールしていた場合に参照ができないらしいです。

なので`sudo pip3 install schedule`という風に**スーパーユーザーで実行する**ことでrootにインストールができ、systemd側が見つけられるらしいです。

## 大変参考にしたサイト様

### プログラム作成
* [LineBotの作り方（python）](https://datadriven-rnd.com/linebot/)
* [Python で 天気予報APIからお天気情報を取得してみよう](https://kenkyujinsei.com/2021/02/06/python-%e3%81%a7-%e5%a4%a9%e6%b0%97%e4%ba%88%e5%a0%b1api%e3%81%8b%e3%82%89%e3%81%8a%e5%a4%a9%e6%b0%97%e6%83%85%e5%a0%b1%e3%82%92%e5%8f%96%e5%be%97%e3%81%97%e3%81%a6%e3%81%bf%e3%82%88%e3%81%86/)
* [Scheduleモジュールを用いたイベント定期実行](https://di-acc2.com/programming/python/4574/)

### ファイルの自動起動設定
* [Raspberry Piでプログラムを自動起動する5種類の方法を比較・解説](https://qiita.com/karaage0703/items/ed18f318a1775b28eab4)
* [Raspberry Pi4起動時に指定したプログラムを実行させる](https://www.pc-koubou.jp/magazine/52061)
* [systemdを使ってスクリプト自動起動](https://monomonotech.jp/kurage/raspberrypi/systemd_autostart.html)
* [systemdによる自動起動（Linux）](https://www.souichi.club/technology/systemd/)
* [【python】pip install scheduleでインストールしたモジュールが読み込まれない](https://teratail.com/questions/125792)

### 天気APIの使用元
* [天気予報 API（livedoor 天気互換）](https://weather.tsukumijima.net/)
