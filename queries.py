import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todoproject.settings")

application = get_wsgi_application()

from todo.models import *
'''
def todolistall():
    t=Todolist.objects.values_list('name')
    print t
    items=[]
    for i in t:
        l=Todolistitem.objects.values_list('description','duedate').filter(parent__name__iexact=i[0])
        s=[i,l]
        items.append(s)
    print items

todolistall()
'''

from django.template import Context,Template
l=['mahendar','reddy']
t=Template("my name is {% for i in list %}\n"
           "name:{{ i }}{% endfor %}")
c=Context({'list':l})
text=t.render(c)
print text






