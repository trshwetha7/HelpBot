FROM huggingface/transformers-pytorch-gpu

WORKDIR /app
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install Streamlit
RUN pip install streamlit

# Install Transformers library
RUN pip install transformers

EXPOSE 8501

CMD ["streamlit", "run", "--server.address=0.0.0.0", "--server.port=8501", "gpt2_app.py"]

