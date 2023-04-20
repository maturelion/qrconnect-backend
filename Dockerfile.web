FROM python:3.9.6-alpine3.14

WORKDIR /backend

RUN python -m pip install --upgrade pip setuptools wheel
RUN apk add --update \
    # psycopg2 dependencies
    --virtual \
    build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    build-base 
# Pillow dependencies
# jpeg-dev \
# zlib-dev \
# freetype-dev \
# lcms2-dev \
# openjpeg-dev \
# tiff-dev \
# tk-dev \
# tcl-dev \
# Cryptography dependencies
# libffi-dev \
# openssl-dev \
# cargo

COPY requirements.txt /backend/
RUN pip install -r requirements.txt


COPY /backend/.env /backend/backend/.env

COPY . /backend/
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["gunicorn", "--workers", "3", "backend.wsgi:application"]