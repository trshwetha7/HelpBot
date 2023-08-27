FROM python:3.8

WORKDIR /app
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install Streamlit and Transformers library
RUN pip install streamlit transformers

EXPOSE 8501

CMD ["streamlit", "run", "--server.address=0.0.0.0", "--server.port=8501", "gpt2_app.py"]

