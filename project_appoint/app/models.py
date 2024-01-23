from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=100)
    reason = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    

