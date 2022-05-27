FROM ubuntu:latest
WORKDIR /app_generic

RUN apt-get update -y 
RUN apt-get install -y python3 python3-pip
COPY dependencies.txt .
RUN pip install -r dependencies.txt
COPY app/ .
ENTRYPOINT python3 webserver.py