import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

st.title("HelpBot")

tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
model = GPT2LMHeadModel.from_pretrained("gpt2-medium")

user_input = st.text_input("You:", "Type your message here...")

if st.button("Reply"):
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    st.text_area("HelpBot:", value=output_text, height=200)

