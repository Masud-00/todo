from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView,FormView
from .models import Task
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .forms import Registetion,Taskform,LoginForm

# Create your views here.

#login

class Tasklogin(LoginView):
    form_class=LoginForm
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('home')

#register

class Taskregister(FormView):
    template_name='base/register.html'
    form_class=Registetion
    redirect_authenticated_user=True
    success_url=reverse_lazy('home')


    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(Taskregister,self).form_valid(form)
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Taskregister,self).get(*args,**kwargs)    

#home

class TaskList(LoginRequiredMixin,ListView):
    model=Task
    template_name='base/index.html'
    context_object_name='tasks'
    ordering=['complete']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] =context['tasks'].filter(user=self.request.user) 
        context['count'] =context['tasks'].filter(complete=False).count()

        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']=context['tasks'].filter(title__startswith=search_input)

        context['search_input']=search_input

        return context    
    

#details

class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    template_name='base/homeDetail.html'
    context_object_name='task'


#add task

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    form_class=Taskform
    template_name='base/create.html'
    success_url='/'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

#update task

class Taskupdate(LoginRequiredMixin,UpdateView):
    model=Task
    form_class=Taskform
    template_name='base/update.html'
    context_object_name="form"
    success_url='/'


#delete task

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    template_name='base/delete.html' 
    context_object_name='task'
    success_url=reverse_lazy('home')
        
