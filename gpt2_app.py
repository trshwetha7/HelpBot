import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
model = GPT2LMHeadModel.from_pretrained("gpt2-medium")

st.title("HelpBot")

user_input = st.text_input("You:", placeholder="Type your message here...")


if st.button("Reply"):
    # Encode and process the user input
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    
    # Generate a response from the model with top-k and top-p sampling
    output = model.generate(
        input_ids, 
        max_length=150, 
        num_return_sequences=1, 
        pad_token_id=tokenizer.eos_token_id,
        top_k=50, 
        top_p=0.95, 
        temperature=0.7
    )
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    
    st.text_area("ChatBot:", value=response, height=200)


