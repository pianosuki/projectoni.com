FROM python:3.11

WORKDIR /code
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN flask db upgrade
CMD ["gunicorn", "wsgi:application", "--bind", "0.0.0.0:80", "--pythonpath", "/code"]
