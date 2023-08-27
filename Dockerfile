# Use a slim Python 3.8 base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev

# Upgrade pip
RUN pip install --upgrade pip

# Install necessary Python libraries
RUN pip install streamlit transformers

# Expose the Streamlit default port
EXPOSE 8501

# Define the command to run the app
CMD ["streamlit", "run", "--server.address=0.0.0.0", "--server.port=8501", "gpt2_app.py"]
