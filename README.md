# Getting started #
## With Docker
- make sure Docker is running
- run `docker-compose up --build` to build the app's docker image
- run `docker-compose up` to start the app
- app listens at `http://127.0.0.1:8000`
## Without Docker
- install `pipenv` to manage dependencies
- run `pipenv install` to install the app dependencies
- run `pipenv run python manage.py runserver` to start the app
- app listens at `http://127.0.0.1:8000`
