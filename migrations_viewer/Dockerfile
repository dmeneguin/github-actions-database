FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /migrations_viewer/requirements.txt

WORKDIR /migrations_viewer

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . /migrations_viewer

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]