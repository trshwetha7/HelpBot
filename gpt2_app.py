import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel

model_name = "gpt2-medium"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

st.title("HelpBot")

user_input = st.text_input("You:", "Type your message here...")

if st.button("Reply"):
    # Encode the input text
    input_ids = tokenizer.encode(user_input, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate a response from the model
    output = model.generate(input_ids, max_length=200, pad_token_id=tokenizer.eos_token_id, num_return_sequences=1)
    
    # Decode the response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    
    st.text_area("HelpBot:", value=response, height=200)

