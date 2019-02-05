#we are gonna be basing the line from
FROM python:3.7-alpine

#who is developing this app
MAINTAINER Oscar Garza

ENV PYTHONUNBUFFERED 1

# using . means local machine other means docker

COPY ./requirements.txt /requirements.txt
#it uses the package manager 'apk' and add a package
RUN apk add --update --no-cache postgresql-client
#set ups an alias for the dependecies and make it easy to remove that dependency later
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps


RUN mkdir /app
WORKDIR /app
COPY ./app /app

#security processes otherwise will use root
RUN adduser -D user
USER user
