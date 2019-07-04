from django.db import models

# Create your models here.

class Appointments(models.Model):
    task = models.CharField(max_length=800, null=False)
    updated_on = models.DateTimeField(auto_now=True)
    appointment_on = models.DateTimeField(null=False, blank=False)


