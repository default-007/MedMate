from django.db import models
from authentication import User


class Patient(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient")

    def __str__(self):
        return self.patient.get_full_name()


class Doctor(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor")

    def __str__(self):
        return self.doctor.get_full_name()


class Pharmacist(models.Model):
    pharmacist = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="phrmacist"
    )

    def __str__(self):
        return self.pharmacist.get_full_name()
