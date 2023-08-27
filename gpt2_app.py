
import streamlit as st
import gpt_2_simple as gpt2


st.title("HelpBot")

user_input = st.text_input("You:", "Type your message here...")

if st.button("Reply"):
    # Assuming the 'sess' variable is available globally
    response = gpt2.generate(sess, model_name="124M", prefix=user_input, length=100, return_as_list=True)[0]
    st.text_area("HelpBot:", value=response, height=200)
