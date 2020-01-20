FROM ubuntu:latest

LABEL version="1.0"
LABEL description="programmation de solution de n-dame"

RUN apt-get update &&\
pip3 install python3

COPY Dame.py /Dame.py
