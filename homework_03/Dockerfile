#For check app - use http://127.0.0.1:8000/ping/ in browser

FROM python:3.9-buster

CMD python -V

WORKDIR /var/main

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt


CMD uvicorn main:app --host=0.0.0.0