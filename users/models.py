from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
