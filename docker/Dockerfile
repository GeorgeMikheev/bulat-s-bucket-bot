FROM python:3.12.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y python3-dev gcc libc-dev libffi-dev && \
    apt-get -y install libpq-dev gcc

COPY ../src/requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ../src .