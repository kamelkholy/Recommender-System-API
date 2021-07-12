FROM python:3.9
WORKDIR /code                 
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./ 
COPY Pipfile Pipfile.lock ./ 
RUN pipenv install
COPY . ./
EXPOSE 8000

CMD pipenv run python manage.py runserver 0.0.0.0:8000