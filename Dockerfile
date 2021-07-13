# syntax=docker/dockerfile:1.0
# Consider using 3.9.6-slim for production usage
FROM python:3.9.6

LABEL author="Justin Casso <justincasso1@gmail.com>"
LABEL description="An Postfix email server that uploads emails to an S3 bucket"
LABEL version="0.1"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -yq \
        postfix=3.4.14-0+deb10u1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install -r /app/requirements.txt

CMD [ "/app/startup.sh" ]

EXPOSE 25
