# TwitterOAuth_Streamlit
StreamlitにTwitter API v.1.1のOAuth認証機能を搭載するためのコード



## How to Use

### 環境の構築

```
git clone https://github.com/tksakaki/TwitterOAuth_Streamlit.git
cd TwitterOAuth_Streamlit
pipenv install
```

### Twitterアプリの登録

1.   (Twitter Developerとしての登録がない場合)[Twitter Developer Platform](https://developer.twitter.com/ja)にて，Twitter Developerとして登録する
2.    [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard) で新たなアプリを作成する
3.   作成したアプリの "Keys and tokens" タブで **ConsumerKey**/ **ConsumerSecret** を取得する
4.   作成したアプリの "Settings"タブの "User authentication settings"にて **Callback URI(Redirect URL)** を` http://localhost:8501`に設定する
     1.   MacOSの一部のバージョン（MojaveやCatalina等）では，localhostが使えないことがある．その場合は、`http://127.0.0.1:8501`を代わりに設定する
5.   `TwitterOAuth_Streamlit/streamlit_twitter_oauth.py` の `consumer_key`, `consumer_secret` を3で取得した値に設定する
     1.   APIのトークンをコード内にベタ書きするのは望ましくないため，dotenvパッケージなどを利用して外部ファイルに記述することを推奨します
     2.   必要があれば `callback_url`を `http://127.0.0.1:8501`に変更する

### サンプルアプリの実行

*   streamlitでサンプルアプリを起動する

```
pipenv run streamlit run app_sample.py
```

*   ブラウザで `http://localhost:8501` もしくは `http://127.0.0.1:8501`にアクセスする
*   「本アプリとのTwitter連携を認証する」の後の「認証する」をクリック
*   twitter.com上で「Authorize」をクリックする
*   **Access Token** と **Access Token Secret**  がブラウザ上に表示される

 ### 注意点

*   起動するStreamlitアプリのURL（http://localhost:8501）と[Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard) のアプリ管理画面で登録する**Callback URI(Redirect URL)** は同一のURLにすること
    *   アプリの管理画面では複数のCallbackURLが登録できるが，一番上に登録すること
