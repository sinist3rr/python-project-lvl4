install:
	@poetry install

run:
	poetry run python manage.py runserver

test:
	poetry run pytest --cov-report html --cov-report xml --cov=task_manager

lint:
	poetry run flake8 task_manager
	poetry run mypy task_manager

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

deploy:
	git push heroku main

.PHONY: install test lint selfcheck check build
