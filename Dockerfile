FROM python:3.10-slim-buster

COPY . /sqlite_query_executor

RUN pip install --upgrade pip
#RUN pip install -r /sqlite_query_executor/requirements.txt 

WORKDIR /sqlite_query_executor
