from datetime import datetime
import email
from pyexpat import model
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone = models.IntegerField(default=0)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name