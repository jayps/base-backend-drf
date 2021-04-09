#!/usr/bin/env bash
#python3 manage.py migrate
#python3 manage.py test
coverage run --source='.' manage.py test
coverage report
