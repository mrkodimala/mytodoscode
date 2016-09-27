import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todoproject.settings")

application = get_wsgi_application()


import click
from todo.models import Todolist,Todolistitem
import datetime

def createtodolist(name):
    print name
    t=Todolist(name=name,created=datetime.date.today().isoformat())
    print t
    t.save()

def createtodolistitem(owner,description,duedate,completed):
    t=Todolist.objects.get(name=owner)
    print owner,description,duedate,t
    tl=Todolistitem(description=description,duedate=duedate,parent=t)
    tl.save()

'''
@click.group()
def cli():
    pass

@cli.command()
def populatedata():
    l=['python','cprogramming','datastructres']
    items=[['learn list','learn tuples','learn dicts','learn decoraters','learn generators'],['laarn pointers','learn algorithms','learn high level recursion'],['learn bst','learn avls','learn b+ tree ']]
    for i in range(0,len(l)):
        createtodolist(l[i])
        for j in items[i]:
            createtodolistitem(i,j,'2016-6-10',False)
    click.echo("Data populated successfully")

@cli.command()
def dropdata():
    Todolist.objects.all().delete()
    click.echo("Data Deleted Successfuuly")


cli=click.CommandCollection(sources=[cli])

if __name__=='__main__':
    cli()
'''
def populatedata():
    l=['python','cprogramming','datastructres']
    items=[['learn list','learn tuples','learn dicts','learn decoraters','learn generators'],['laarn pointers','learn algorithms','learn high level recursion'],['learn bst','learn avls','learn b+ tree ']]
    for i in range(0,len(l)):
        #createtodolist(l[i])
        for j in items[i]:
            createtodolistitem(l[i],j,'2016-6-10',False)
    click.echo("Data populated successfully")

populatedata()
