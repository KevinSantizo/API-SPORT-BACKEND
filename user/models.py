from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser    

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        

class Town(models.Model):
    department = models.ForeignKey(Department, related_name='towns', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ', ' + self.department.name


class Profile(AbstractUser):
    town = models.ForeignKey(Town, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.username