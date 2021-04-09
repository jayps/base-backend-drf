# Base DRF App
This repository serves to be a base application for future projects.

## What's included?
Some batteries:
- JWT authentication
- User management, including a custom user model
- This API is Dockerized

## Getting started
Fork this repo to get started. This app is dockerized, so just run `docker-compose up -d` to start the application. Local development uses `python manage.py runserver`, whereas values like `staging` or `production` for the `environment` environment variable will cause the app to run with a uwsgi server.

## Code formatting
Please run `pre-commit install` before making commits to this repo. That'll helo with formatting.

## Environment variables
The environment variables for this application are as follows:
- `DJANGO_DEBUG`: Sets debug mode on or off. Use `False` for production.
- `ALLOWED_HOSTS`: Comma separated list of allowed hosts for the app. Defaults to `*`, so you should probably set this.
- `POSTGRES_DB`: Database name for Postgres.
- `POSTGRES_USER`: Database username.
- `POSTGRES_HOST`: Database host.
- `POSTGRES_PORT`: Database port.
- `POSTGRES_PASSWORD`: Database password.
- `WORKER_COUNT`: Worker count for WSGI.
- `WORKER_TIMEOUT`: Worker timeout for WSGI.
All these variables are set in the default `docker-compose.yml` file for reference.

## Running commands in the container
Let's take a look at creating a super user as an example.
`docker exec -it base-backend-api python manage.py createsuperuser`
Where `base-backend-api` is the name of your container (run `docker ps` to get this), and `python manage.py createsuperuser` is your command.
You can also bash into the container with `docker exec -it base-backend-api bash` and run commands within the container's environment.
