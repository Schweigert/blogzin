from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

class Post(models.Model):
    body = models.CharField(max_length=10000)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
