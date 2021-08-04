from django.db import models

class contactsave(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    message1=models.TextField(max_length=30)
    message2=models.TextField(max_length=30)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip=models.CharField(max_length=10)
    date=models.DateField()