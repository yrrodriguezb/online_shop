FROM python:3.8.10-buster

WORKDIR /app

COPY src src 

COPY requirements.txt requirements.txt

EXPOSE 8000

RUN pip install -r requirements.txt \
    && python src/manage.py migrate 

CMD [ "python", "src/manage.py", "runserver", "0.0.0.0:8000" ]
