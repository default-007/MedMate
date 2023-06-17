from django.db import models
from authentication.models import User
from simple_history.models import HistoricalRecords


class Patient(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient")
    diagnosis = models.TextField(blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.patient.get_full_name()


class Doctor(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor")
    specialization = models.CharField("Specialisation", max_length=250)
    history = HistoricalRecords()

    def __str__(self):
        return self.doctor.get_full_name()


class Pharmacist(models.Model):
    pharmacist = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="phrmacist"
    )
    registration_no = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=20, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.pharmacist.get_full_name()
