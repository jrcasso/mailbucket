# syntax=docker/dockerfile:1.0
# Consider using 3.9.6-slim for production usage
FROM python:3.9.6-buster

LABEL author="Justin Casso <justincasso1@gmail.com>"
LABEL description="A Postfix email server that uploads emails to an S3 bucket"
LABEL version="1.0"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -yq \
        postfix=3.4.14-0+deb10u1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY scripts/healthcheck.sh /app/healthcheck.sh
COPY config/master.cf /etc/postfix/master.cf
COPY config/main.cf /etc/postfix/main.cf
COPY requirements.txt /app/requirements.txt
COPY upload.py /app/upload.py

RUN pip install -r /app/requirements.txt

CMD [ "postfix", "start-fg" ]

EXPOSE 25/tcp
