from django.db import models
from datetime import datetime
# Create your models here.
class contactus(models.Model):
    fullname=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    details=models.CharField(max_length=255)

    currentdate=models.DateTimeField( blank=True,default=datetime.now)
    def __str__(self):
        return self.email