FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install streamlit transformers

EXPOSE 8501

# Define the command to run the app
CMD ["streamlit", "run", "--server.address=0.0.0.0", "--server.port=8501", "gpt2_app.py"]
