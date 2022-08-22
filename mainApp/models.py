from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    dsg = models.CharField(max_length=20)
    salary = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
