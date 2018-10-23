from django.db import models

# Create your models here.

class Group(models.Model):
    def __str__(self):
        return "group: " + self.name
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Event(models.Model):
    def __str__(self):
        return "Event: " + self.name
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
