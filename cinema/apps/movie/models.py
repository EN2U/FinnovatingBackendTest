from os import remove
from django.db import models

from cinema.apps.establishment.models import Establishment


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    premiere_date = models.DateField()
    expiration_date = models.DateField()
    duration = models.PositiveSmallIntegerField()
    cinema = models.ForeignKey(Establishment, on_delete=models.CASCADE)