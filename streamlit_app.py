import streamlit as st

st.set_page_config(page_title="TrivAI App", layout="centered")

st.title("🦋 Welcome to TrivAI!")
st.subheader("A blend of emotions and logics, built with love and purpose.")

user_input = st.text_input("Ask something:")
if user_input:
    st.success(f"You said: {user_input}")
    st.info("Note: This is a demo. More features coming soon!")

st.markdown("📌 For help and inspiration, visit [docs.streamlit.io](https://docs.streamlit.io/)")
