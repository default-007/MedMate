from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="patient"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(blank=True)
    weight = models.IntegerField()


class Healthcare_Providers(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="healthcare provider",
    )
    full_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField()
    physical_address = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
