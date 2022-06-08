from tkinter import CASCADE
from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)

class Newsletter(models.Model):
    id = models.UUIDField(primary_key=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    price = models.FloatField()
