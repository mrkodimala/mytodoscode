from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from views import ViewTodoList,Show_Items,Add_List,Add_List_Items,Update_List_Items,Delete_List_item,Update_List,Delete_List

from . import views

urlpatterns = [
    url(r'^todolist/$',(ViewTodoList.as_view()),name='todolistall'),
    url(r'^todolist/(?P<item>[0-9]+)/$',Show_Items.as_view(),name='showitems'),
    url(r'^todolist/addlist/$',Add_List.as_view(),name='addlist'),
    url(r'^todolist/updatelist/(?P<id>[0-9]+)/$',Update_List.as_view(),name='updatelist'),
    url(r'^todolist/deletelist/(?P<id>[0-9]+)/$',Delete_List.as_view(),name='deletelist'),
    url(r'^todolist/(?P<item>[0-9]+)/add/$',Add_List_Items.as_view(),name='addlistitems'),
    url(r'^todolist/(?P<item>[0-9]+)/update/(?P<id>[0-9]+)/$', Update_List_Items.as_view(), name='updatelistitems'),
    url(r'^todolist/(?P<item>[0-9]+)/delete/(?P<id>[0-9]+)/$',Delete_List_item.as_view(), name='deletelistitems'),
]