import streamlit as st
from streamlit_twitter_oauth import twitter_oauth2_required

@twitter_oauth2_required
def main():
    access_token = st.session_state.access_token
    access_token_secret = st.session_state.access_token_secret
    st.text(f'You\'re logged in!')
    st.text(f'Access Token: {access_token}')
    st.text(f'Access Token Secret: {access_token_secret}')


main()