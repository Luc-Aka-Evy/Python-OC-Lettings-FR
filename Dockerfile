FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/

RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app/

CMD ["python3", "manage.py", "runserver"]