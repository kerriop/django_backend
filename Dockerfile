FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk --update add
RUN apk add gcc libc-dev libffi-dev jpeg-dev zlib-dev libjpeg
RUN apk add postgresql-dev

RUN pip install --upgrade pip

COPY ./Pipfile.lock .

RUN pip install pipenv
RUN pipenv sync

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
