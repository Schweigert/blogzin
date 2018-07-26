# How this is constructed

Bootstrap

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
