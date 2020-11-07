# Aaltoileva

## Description
A website that acts as a demo for the Aaltoileva app. The app asks its users how they're feeling and if they're eg. stressed about their studies, after which it presents anonymized data about how other users are feeling. The purpose of the app is to increase the wellbeing of students by lowering their sense of emotional isolation.

https://youtu.be/MfY4NVVWlk0

### Built With
- Django 3.1.3 (back-end)
- Python 3.9 (back-end)
- CSS (front-end)
- HTML (front-end)  

## Installation
Step 1: Clone Project

    $ git clone https://github.com/tonipel/aaltomood.git

Step 2: Install dependencies

    $ pip install -r requirements.txt

Step 3: Apply migrations

    $ python manage.py migrate

Step 4: Run server
    
    $ python manage.py runserver


## Development

### Create a user
    $ python manage.py add_admin_user -u admin -p admin -e admin@example.com


### Create migrations

    $ python manage.py makemigrations

