FROM python:3.8.10-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src src 

ENV DJANGO_SETTINGS_MODULE="shop.settings.production"

EXPOSE 8000

COPY ./compose/django/entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT [ "entrypoint.sh" ]

CMD [ "python", "src/manage.py", "runserver", "0.0.0.0:8000" ]