import streamlit as st
import tweepy

callback_url = 'http://localhost:8501'
#callback_url = 'http://127.0.0.1:8501' 
# MacOSの一部のバージョン（MojaveやCatalina等）では，localhostが使えないためこちらを利用する

consumer_key = '[ConsumerKey]'
consumer_secret = '[ConsumerSecret]'


def twitter_oauth2_required(func):
    def wrapper(*args, **kwargs):

        oauth1_user_handler = tweepy.OAuth1UserHandler(
            consumer_key, 
            consumer_secret, 
            callback_url
            )
        authorization_url = oauth1_user_handler.get_authorization_url(signin_with_twitter=True)

        if 'access_token' not in st.session_state:
            st.session_state.access_token = None

        if st.session_state.access_token is None:
            query_params = st.experimental_get_query_params()
            try:
                # URLから oauth_token を取り出して、auth.request_token[‘oauth_token’] にセット
                oauth_token = query_params['oauth_token'][0]
                oauth1_user_handler.request_token['oauth_token'] = oauth_token

                # URLから、oauth_verifierを取り出して、oauth_token_secretにセット
                oauth_verifier = query_params['oauth_verifier'][0]
                oauth1_user_handler.request_token['oauth_token_secret'] = oauth_verifier

                # access_token, access_token_secretを取得
                access_token, access_token_secret = oauth1_user_handler.get_access_token(oauth_verifier)

                # 取得した access_token, access_token_secret を表示しつつ，セッション情報として保存
                st.text(f"{access_token}, {access_token_secret}")
                st.session_state.access_token = oauth1_user_handler.access_token
                st.session_state.access_token_secret = oauth1_user_handler.access_token_secret
            except Exception as e:
                st.text(str(e.args))
                st.json(query_params)
                st.write(
                    f"""<h1>
                    本アプリとのTwitter連携を認証する <a target="_self"
                    href="{authorization_url}">認証する</a></h1>""",
                    unsafe_allow_html=True,
                )

        else:
            func(*args, **kwargs)

    return wrapper
