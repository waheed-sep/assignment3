FROM python:latest

MAINTAINER Sohaib "sohaibayub9@gmail.com"

ADD . /docker_learning

WORKDIR /docker_learning

RUN pip install -r requirements.txt

ENTRYPOINT python3 app.py
