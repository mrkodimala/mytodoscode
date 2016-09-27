from django.contrib import admin

# Register your models here.
from .models import Todolist,Todolistitem

admin.site.register((Todolist,Todolistitem))