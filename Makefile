install:
	@poetry install

run:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

test:
	poetry run pytest --cov-report xml --cov=task_manager --cov=users --cov=statuses --cov=tasks --cov=labels users/tests.py statuses/tests.py tasks/tests.py labels/tests.py

lint:
	poetry run flake8 --exclude=*/migrations/* task_manager users statuses tasks labels
	poetry run mypy task_manager users statuses tasks labels

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

deploy:
	git push heroku main

.PHONY: install test lint selfcheck check build
