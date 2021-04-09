#!/usr/bin/env bash
sleep 10
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:8000 base_backend.wsgi --reload --workers=$WORKER_COUNT --timeout=$WORKER_TIMEOUT
