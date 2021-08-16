# Проект "Менеджер задач"

---
[![Maintainability](https://api.codeclimate.com/v1/badges/7f9a540e7cf3fd7c2efd/maintainability)](https://codeclimate.com/github/sinist3rr/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7f9a540e7cf3fd7c2efd/test_coverage)](https://codeclimate.com/github/sinist3rr/python-project-lvl4/test_coverage)
![Build_and_Test](https://github.com/sinist3rr/python-project-lvl4/workflows/build%20&%20test/badge.svg)

### Hexlet tests and linter status:
[![Actions Status](https://github.com/sinist3rr/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/sinist3rr/python-project-lvl4/actions)

### Installation
* Install [poetry](https://python-poetry.org/docs/#installation)
* ```git clone https://github.com/sinist3rr/python-project-lvl4.git```
* ```cd python-project-lvl4/ && make install && make migrate && make run```
***

### URL

[Check online at Heroku](https://ancient-hollows-77564.herokuapp.com/)


### Environment variables

| Variable               | Used value                          | Description                                                                |
|------------------------|-------------------------------------|----------------------------------------------------------------------------|
| SECRET_KEY             | random secret key                   | set Django secret key                                                      |
| DATABASE_URL           | sqlite:///db.sqlite3                | set the path to DB                                                         |
| DJANGO_SETTINGS_MODULE | task_manager.settings               | tell Django which settings is using                                        |
| ALLOWED_HOSTS          | ancient-hollows-77564.herokuapp.com | a list of strings representing the host/domain names that Django can serve |
| DEBUG                  | -                                   | a boolean that turns on/off debug mode                                     |

