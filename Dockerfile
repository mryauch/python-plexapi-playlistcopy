FROM python:latest

RUN apt-get update

RUN pip install --upgrade pip setuptools
RUN pip install plexapi

ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./run.py /run.py

ENTRYPOINT [ "python", "/run.py" ]
