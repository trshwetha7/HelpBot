FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    libffi-dev \
    libssl-dev \
    python3-dev \
    python3-pip \
    python3-venv

# Upgrade pip
RUN pip install --upgrade pip

# Install Streamlit
RUN pip install streamlit

# Install Transformers
RUN pip install transformers

EXPOSE 8501

CMD ["streamlit", "run", "--server.address=0.0.0.0", "--server.port=8501", "gpt2_app.py"]

