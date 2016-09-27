from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Todolist(models.Model):
    owner=models.ForeignKey(User)
    name=models.CharField(max_length=100)
    created=models.DateField()
    def __str__(self):
        return self.name

class Todolistitem(models.Model):
    description=models.CharField(max_length=150)
    duedate=models.DateField()
    completed=models.BooleanField(default=False)
    parent=models.ForeignKey(Todolist)
    def __str__(self):
        return self.description