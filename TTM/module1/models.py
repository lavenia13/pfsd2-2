from django.db import models

# Create your models here.
class Lavenia(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    class Meta:
        db_table="Lavenia"

class contactus(models.Model):
    firstname=models.TextField(max_length=255)
    Lastname=models.TextField(max_length=255)
    email=models.EmailField(primary_key=True)
    comments=models.TextField(max_length=255)
    class Meta:
        db_table="contactus"