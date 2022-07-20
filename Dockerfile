FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/
RUN python3 manage.py migrate

EXPOSE 8000
CMD ["gunicorn", "oc_lettings_site.wsgi", "--log-file -", "--bind=0.0.0.0:8000"]