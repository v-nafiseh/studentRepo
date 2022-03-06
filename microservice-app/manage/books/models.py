from statistics import mode
from turtle import title
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    