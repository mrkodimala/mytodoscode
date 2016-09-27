from rest_framework import serializers
from todo.models import Todolist,Todolistitem

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todolist
        fields=('id','name','owner','created')

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todolistitem
        fields=('id','description','duedate','completed','parent')


