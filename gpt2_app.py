import streamlit as st

st.title("Simple ChatBot")

responses = {
    "hello": "Hi! How can I help you?",
    "bye": "Goodbye! See you later.",
}

user_input = st.text_input("You:", "Type your message here...")

if st.button("Reply"):
    response = responses.get(user_input.lower(), "Sorry, I don't understand that.")
    st.text_area("ChatBot:", value=response, height=200)

