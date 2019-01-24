#we are gonna be basing the line from
FROM python:3.7-alpine

#who is developing this app
MAINTAINER Oscar Garza

ENV PYTHONUNBUFFERED 1

# using . means local machine other means docker

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

#security processes otherwise will use root
RUN adduser -D user
USER user
