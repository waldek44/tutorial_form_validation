### Projekt tutoriala formularza z walidacją

- editor -> spelling -> dodaję language pack

- instaluję i inicjuję projekt
```
pip install django==2.2

django-admin startproject formularz_demo .

py manage.py runserver

py manage.py makemigrations
py manage.py migrate

py manage.py createsuperuser

pip freeze > requirements.txt
```

#### Commit 1 Tworzę aplikację

- Tworzę aplikację
```
python manage.py startapp main
```

