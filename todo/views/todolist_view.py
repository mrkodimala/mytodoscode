from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms import forms
from django.forms.models import inlineformset_factory
from django.utils.decorators import method_decorator

from todo.models import Todolist,Todolistitem
from django.views.generic import ListView,CreateView,UpdateView,DeleteView


@method_decorator(login_required(),name='dispatch')
class ViewTodoList(ListView):
    model=Todolist
    template_name='todo/todolistall.html'
    context_object_name='items'

    def get_queryset(self):
        return Todolist.objects.filter(owner=self.request.user)


@method_decorator(login_required,name='dispatch')
class Add_List(CreateView):
    model=Todolist
    fields = ('name','created')
    template_name = 'todo/add_list.html'

    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super(Add_List,self).form_valid(form)

    def get_success_url(self):
        return reverse('todolistall')

@method_decorator(login_required,name='dispatch')
class Update_List(UpdateView):
    model=Todolist
    fields = ('name','created')
    template_name = 'todo/add_list.html'

    def get_object(self, queryset=None):
        return Todolist.objects.get(id=self.kwargs.get('id'))

    def get_success_url(self):
        return reverse('todolistall')



@method_decorator(login_required,name='dispatch')
class Delete_List(DeleteView):
    model=Todolist
    template_name = 'todo/delete_item.html'

    def get_object(self, queryset=None):
        return Todolist.objects.get(id=self.kwargs.get('id'))

    def get_success_url(self):
        return reverse('todolistall')



