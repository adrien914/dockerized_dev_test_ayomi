FROM python:2.7.16

COPY ./test_dev /test_dev

WORKDIR /test_dev

RUN pip install -r requirements.txt.

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


