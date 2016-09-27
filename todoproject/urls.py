"""todoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.template.backends import django
from django.views.generic import  TemplateView
from todo.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/',include('todo.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls'),name='authentication'),
    url(r'^todolist/$',todolist),
    url(r'^todolist/(?P<id>[0-9]+)/$',todolistdetails),
    url(r'^todolistitems/(?P<id>[0-9]+)/$',todolistitems),
    url(r'^listitem/(?P<id>[0-9]+)/$',todolistitemsdetail),
    url(r'^backbone/$',TemplateView.as_view(template_name="todo/newtodo.html")),
    url(r'^angular/$',TemplateView.as_view(template_name="angularjsfile.html"))
]
