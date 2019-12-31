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

#### Commit 2 Model danych
> Załóżmy, że istnieje formularz, który przyjmuje Nazwę użytkownika, płeć i tekst jako dane wejściowe od użytkownika, zadaniem jest sprawdzenie danych i zapisanie ich.
> Najpierw tworzę dane.

- robię models.py
- dodaję aplikację do settings.py
- migruję
```
py manage.py makemigrations
py manage.py migrate
```

#### Commit 3 Formularz
> Teraz można utworzyć formularz. Załóżmy, że długość nazwy użytkownika nie powinna być mniejsza niż 5, 
> a długość postu powinna być większa niż 10. Następnie definiujemy Class PostForm z wymaganymi regułami 
> sprawdzania poprawności.

```
pip install django-bootstrap4
```
- tworzę forms.py
- tworzę urls.py
- wypełniam views.py
