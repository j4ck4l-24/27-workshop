FROM python:3

WORKDIR /27-workshop

COPY app.py /27-workshop/
COPY templates /27-workshop/templates/
COPY static /27-workshop/static/
COPY userdb.db /27-workshop/

RUN apt-get update && apt-get install -y sqlite3

RUN pip install Flask

EXPOSE 7000

CMD ["python3", "app.py"]

