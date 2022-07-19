FROM python:3.8
ENV PYTHONUNBUFFERED 1

ADD . /app/
WORKDIR /app
COPY requirements.txt /app/

RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app/
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

VOLUME /app/logs

CMD ["python3", "manage.py", "runserver"]