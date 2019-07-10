#!/bin/sh

python /app/mpage_test/manage.py makemigrations && python /app/mpage_test/manage.py migrate && python /app/mpage_test/manage.py runserver 0.0.0.0:8000
