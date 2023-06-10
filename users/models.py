from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    is_patient = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    email = models.EmailField(_("email address"), unique=True)
    physical_address = models.CharField(max_length=100)
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Patient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="patient"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(blank=True)
    weight = models.IntegerField()

    def __str__(self):
        return self.first_name


class HealthcareProviders(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="healthcare_provider",
    )
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    registration_no = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name
