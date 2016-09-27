from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

from todo.models import Todolist,Todolistitem
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView

@method_decorator(login_required,name='dispatch')
class Show_Items(DetailView):
    model=Todolist
    template_name = 'todo/todolis.html'
    context_object_name = 'listitems'
    def get_context_data(self, **kwargs):
        context= super(Show_Items, self).get_context_data(**kwargs)
        context['items']=self.kwargs.get('item')
        return context

    def get_object(self, queryset=None):
        item=self.kwargs.get('item')
        if item:
            return Todolist.objects.get(id__iexact=item)
        else:
            return Todolist.objects.all()

@method_decorator(login_required,name='dispatch')
class Add_List_Items(CreateView):
    template_name = 'todo/add_list.html'
    model=Todolistitem
    fields = ('description','duedate','completed')

    def form_valid(self, form):
        form.instance.parent=Todolist.objects.get(id=self.kwargs.get('item'))
        return super(Add_List_Items,self).form_valid(form)

    def get_object(self, queryset=None):
        return Todolist.objects.get(id__iexact=self.kwargs.get('item'))

    def get_success_url(self):
        return reverse('showitems',kwargs={'item':self.kwargs.get('item')})

@method_decorator(login_required,name='dispatch')
class Update_List_Items(UpdateView):
    template_name = 'todo/add_list.html'
    model = Todolistitem
    fields = ('description','duedate','completed')

    def form_valid(self, form):
        form.instance.parent = Todolist.objects.get(id=self.kwargs.get('item'))
        return super(Update_List_Items, self).form_valid(form)

    def get_object(self, queryset=None):
        return Todolistitem.objects.get(id__iexact=self.kwargs.get('id'))

    def get_success_url(self):
        return reverse('showitems', kwargs={'item': self.kwargs.get('item')})

@method_decorator(login_required,name="dispatch")
class Delete_List_item(DeleteView):
    template_name = 'todo/delete_item.html'
    model=Todolistitem

    def get_object(self, queryset=None):
        return Todolistitem.objects.get(id__iexact=self.kwargs.get('id'))
    def get_success_url(self):
        return reverse('showitems', kwargs={'item': self.kwargs.get('item')})




