#!/bin/sh

python /app/masivian_tst/manage.py makemigrations && python /app/masivian_tst/manage.py migrate && python /app/masivian_tst/manage.py runserver 0.0.0.0:8000
