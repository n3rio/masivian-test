from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    review = models.CharField(max_length=300)
