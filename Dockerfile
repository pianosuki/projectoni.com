FROM python:3.11

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/app
RUN apt update && apt install -y gunicorn
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:80"]