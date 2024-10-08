FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install -y awscli -y

RUN pip install -r requirements.txt

CMD [ "python3", "app.py" ]
