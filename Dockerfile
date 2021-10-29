FROM python:3.7-buster

EXPOSE 8022

COPY . /recommender

WORKDIR /recommender

RUN pip install -r ./requirements.txt
