FROM python:3.8

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install -r /app/requirements.txt

# copy project
COPY ./src /app

