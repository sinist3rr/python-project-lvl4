install:
	@poetry install

run:
	poetry run python manage.py runserver

test:
	export DJANGO_SETTINGS_MODULE=task_manager.settings
	poetry run pytest --cov-report xml --cov=task_manager users/tests.py statuses/tests.py tasks/tests.py labels/tests.py

lint:
	poetry run flake8 --exclude=*/migrations/* task_manager users statuses tasks labels
	poetry run mypy task_manager

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

deploy:
	git push heroku main

.PHONY: install test lint selfcheck check build
