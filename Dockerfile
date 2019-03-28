#we are gonna be basing the line from
FROM python:3.7-alpine

#who is developing this app
MAINTAINER Oscar Garza

ENV PYTHONUNBUFFERED 1

# using . means local machine other means docker

COPY ./requirements.txt /requirements.txt

#these dependencies are permanent
#it uses the package manager 'apk' and add a package
RUN apk add --update --no-cache postgresql-client jpeg-dev
#set ups an alias for the dependecies and make it easy to remove that dependency later
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps


RUN mkdir /app
WORKDIR /app
COPY ./app /app

#security processes otherwise will use root
# -p os for creating the whole path
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
#it sets ownership of vol directory to our user -R is for recursive
RUN chown -R user:user /vol
# permission to other users
RUN chmod -R 755 /vol/web
USER user
