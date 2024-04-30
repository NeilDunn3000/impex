from django.db import models

# Create your models here.

class Manufacturers(models.Model):

    Division = models.CharField(max_length=150)
    Description = models.CharField(max_length=225)
    date_2012 = models.CharField(max_length=150)
    date_2022 = models.CharField(max_length=150)

