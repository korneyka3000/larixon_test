#!/usr/bin/sh

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata db.json

python manage.py create_admin

python manage.py runserver 0.0.0.0:8000

