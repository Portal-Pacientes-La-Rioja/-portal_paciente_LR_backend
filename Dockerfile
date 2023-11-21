FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
# Use Debian

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip install mysqlclient

COPY ./app /code/app

COPY ./alembic /alembic

COPY ./alembic.ini /alembic

COPY ./templates/ /code/app/templates/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]

