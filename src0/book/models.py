from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
