# How this is constructed

## Bootstrap

```sh
# Start project
pipenv install

# Install django
pipenv install django

# Start project
pipenv run django-admin startproject blogzin

# Move all files to root
mv blogzin /.*

# Remove blogzin folder
rm -rf blogzin

# Create blog app
pipenv run python manage.py startapp blog

# Run Server
pipenv run python manage.py runserver 0:8000
```

## Admin

run migrations:

```sh
pipenv run python manage.py migrate
```

create superuser:

```sh
pipenv run python manage.py createsuperuser

# Defaults in DB
# marlon
# marlon.henry@magrathealabs.com
# nopassword123123
# nopassword123123
```

```python
# urls.py
from django.conf.urls import url
from django.contrib import admin
from blogzin.blog import *

urlpatterns = [
    url('admin/', admin.site.urls),
]
```

## Home

Views and routes:

```python
# blog/views.py
from django.http import HttpResponse

def blog_index(request):
    return HttpResponse("My blog is alive!")

# urls.py
from django.conf.urls import url
from django.contrib import admin
from blogzin.blog import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', blog_index, name='home'),
]
```

## Models

```python
# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogzin.blog',
]


# blog/models.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

class Post(models.Model):
    body = models.CharField(max_length=10000)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

Create migrations:

```sh
pipenv run python manage.py makemigrations blog
pipenv run python manage.py migrate
```
