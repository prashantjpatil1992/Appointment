from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=100)
    reason = models.CharField(max_length=300)
    appoint_date = models.CharField(max_length=100,null=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    slot = models.CharField(max_length=5,null=True)

class AppointmentHistory(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=100)
    reason = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    slot = models.CharField(max_length=5,null=True)

class TimeSlot(models.Model):
    slots = models.CharField(max_length=20)

class AvailableDates(models.Model):
    dates = models.CharField(max_length=100)
    

