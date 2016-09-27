from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

from .models import *

def todolist(request,owner):
    l=Todolistitem.objects.filter(parent__name__iexact=owner)
    template=get_template('todo/todolist.html')
    return HttpResponse(template.render(context={'listitems':l,'listname':owner}))

def todolistall(request):
    t = Todolist.objects.all()
    #print t
    #items = []
    #for i in t:
    #    l = Todolistitem.objects.values_list('description', 'duedate').filter(parent__name__iexact=i[0])
    #    s = [i, l]
    #    items.append(s)
    template=get_template('todo/todolistall.html')
    return HttpResponse(template.render(context={'items':t}))
