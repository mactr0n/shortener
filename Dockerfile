FROM python:3-alpine3.10

COPY requirements.txt shortener.py /app/

RUN pip3 install -r /app/requirements.txt

WORKDIR /app

ENV FLASK_APP=shortener.py

EXPOSE 5000

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]