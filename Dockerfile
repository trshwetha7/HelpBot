
FROM tensorflow/tensorflow:1.15.0-py3

WORKDIR /app

COPY . .

RUN pip install streamlit gpt-2-simple

EXPOSE 8501

CMD ["streamlit", "run", "gpt2_app.py"]
