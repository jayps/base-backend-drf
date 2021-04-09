# Base DRF App
This repository serves to be a base application for future projects.

## What's included?
Some batteries:
- Automated documentation (at `/swagger` and `/redoc`)
- JWT authentication
- User management, including a custom user model
- This API is Dockerized

## Getting started
Fork this repo to get started. This app is dockerized, so just run `docker-compose up -d` to start the application. Local development uses `python manage.py runserver`, whereas values like `staging` or `production` for the `environment` environment variable will cause the app to run with a uwsgi server.

# TODO:
- Example endpoints and models, including unit tests. Consider using users endpoints for this kind of thing.
- Permissions system.

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
- `DJANGO_SETTINGS_MODULE`: Settings module to use. Useful for stuff like switching out settings during testing.
All these variables are set in the default `docker-compose.yml` file for reference.

## Running commands in the container
Let's take a look at creating a super user as an example.
`docker exec -it base-backend-api python manage.py createsuperuser`
Where `base-backend-api` is the name of your container (run `docker ps` to get this), and `python manage.py createsuperuser` is your command.
You can also bash into the container with `docker exec -it base-backend-api bash` and run commands within the container's environment.

## Running tests
Just run `docker-compose -f docker-compose.test.yml up`

## Adding dependencies
Now and then, you might need to install a new pip library. Remember to run `docker-compose up --build` in order to install your new dependencies in the container.
Also, we know it's easy to just install modules. Please e mindful of what you're adding.
