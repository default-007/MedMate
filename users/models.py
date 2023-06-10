from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    is_patient = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True, related_name="patient"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    email = models.EmailField(_("email address"), unique=True)

    contact = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(blank=True)
    weight = models.IntegerField()
    USERNAME_FIELD = "email"
    REQUIRED_FIELD = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class HealthcareProviders(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="healthcare provider",
    )
    full_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField()
    is_active = models.BooleanField(default=False)
    physical_address = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "registration_no"
    REQUIRED_FIELD = []

    objects = CustomUserManager

    def __str__(self):
        return self.full_name
