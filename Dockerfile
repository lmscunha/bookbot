# Base Image
FROM python:3.11-slim-buster

# Set working directory
WORKDIR /app

# Copy the necessary files into the image
COPY main.py .
COPY books/ ./books/
COPY Pipfile .
COPY Pipfile.lock .

# Set env variables
ENV BOOK_PATH=./books/frankenstein.txt

# Update apt
RUN apt-get update -y && apt-get upgrade -y

# Install build tooling
RUN apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev 

# Install pipenv
RUN pip install pipenv

# Install dependencies using pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# Run our Python script
CMD ["python3", "main.py"]

