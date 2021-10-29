FROM python:3.9.7-buster

EXPOSE 8022

COPY ./requirements.txt /recommender/requirements.txt

WORKDIR /recommender

RUN pip install -r ./requirements.txt

COPY . /recommender/

