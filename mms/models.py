from django.db import models


# Create your models here.
class Institution(models.Model):
    name = models.CharField(
        max_length=10,
    )


class Schedule(models.Model):
    day = models.CharField(max_length=50)
