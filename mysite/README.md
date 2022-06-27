# # Shipments (backend part)

## Table of Contents

1. Description
2. Instructions
3. Running
4. Important Points

## Description

- it represents a shipment website ,could be used by custom users

# Instructions

- run `python3 -m venv venv` to create virtual enviroment and `source venv/bin/activate` to activate it
- `cd` into your app and run these commands : `pip install -r requirementstxt`
- change your setting file to match your configrations of your database ,
  follow (https://pypi.org/project/django-cors-headers/) steps for cors-headers configrationin your setting file
- `cd` into your app and run `python3 manage.py makemigrations` then `python3 manage.py migrate`

# Running

- start server with `python3 manage.py runserver` to launch.
- open `http://127.0.0.1:8000/` in the browser.
