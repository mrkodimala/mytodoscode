from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo.models import *
from todo.serializers import *

@login_required
@api_view(['GET','POST'])
def todolist(request):
    if request.method=='GET':
        todos=Todolist.objects.filter(owner=request.user)
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data=request.data
        data['owner']=request.user.id
        print(data)
        serializer=TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET','PUT','DELETE'])
def todolistdetails(request,id):
    try:
        todos=Todolist.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        t=TodoSerializer(todos)
        return Response(t.data)
    elif request.method=='PUT':
        data=request.data
        data['owner']=request.user.id
        s=TodoSerializer(todos,data=data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        todos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@login_required
@api_view(['GET','POST'])
def todolistitems(request,id):
    if request.method=='GET':
        todoitems=Todolistitem.objects.filter(parent_id=id)
        ser=TodoItemSerializer(todoitems,many=True)
        return Response(ser.data)
    elif request.method=='POST':
        data=request.data
        data['parent']=id
        ser=TodoItemSerializer(data=data)
        if ser.is_valid():
            ser.save()
            todoitems = Todolistitem.objects.filter(parent_id=id)
            ser = TodoItemSerializer(todoitems, many=True)
            return Response(ser.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

@login_required
@api_view(['DELETE'])
def todolistitemsdetail(request,id):
    try:
        todoitem=Todolistitem.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        todoitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)