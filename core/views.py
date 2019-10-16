from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse #nova
#25/09 - Tentando primeiro Crud
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from django.http import HttpResponseRedirect



# Create your views here.



def login(request):
    return render(request, 'login.html')


def inicio(request):
    return render(request, 'inicio.html')

# DIVISAO CRUD
#  Create
def divisao_create(request):
    submitted = False
    if request.method == 'POST':
        form = DivisaoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
             # assert False
            form.save()
            return HttpResponseRedirect('/divisaolist')
    else:
        form = DivisaoForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'core/divisao_create.html', {'form': form, 'submitted': submitted})



#List
class DivisaoListView(ListView):
    model = Divisao
template_name = "base.html"
  

#Update
def divisao_update(request, codigo):
    post = get_object_or_404(Divisao, pk=codigo)
    if request.method == "POST":
        form = DivisaoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False) 
            post.save()
            return redirect('/divisaolist')
    else:
        form = DivisaoForm(instance=post)
    return render(request, 'core/divisao_create.html', {'form': form})
    

# Delete
def divisao_delete (request, codigo):
     post = get_object_or_404 (Divisao, pk = codigo)
     post.delete ()
     return redirect ('/divisaolist')

###################################### FIM CRUD DIVISÃO ######################################
##############################-------------------------------#################################

#CRUD SEÇÃO 
#List
class SecaoListView(ListView):
    model = Secao
template_name = "base.html"

#Update
def secao_update(request, secao_codigo):
    post = get_object_or_404(Secao, pk=secao_codigo)
    if request.method == "POST":
        form = SecaoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False) 
            post.save()
            return redirect('/secaolist')
    else:
        form = SecaoForm(instance=post)
    return render(request, 'core/secao_create.html', {'form': form})
    

# Delete
def secao_delete (request, secao_codigo):
     post = get_object_or_404 (Secao, pk = secao_codigo)
     post.delete ()
     return redirect ('/secaolist')

def secao_create(request):
    submitted = False
    if request.method == 'POST':
        form = SecaoForm(request.POST)
        if form.is_valid():        
            cd = form.cleaned_data
             # assert False
            form.save()
            return HttpResponseRedirect('/secaolist')
    else:
        form = SecaoForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'core/secao_create.html', {'form': form, 'submitted': submitted})

###################################### FIM CRUD SEÇÃO ######################################
##############################-------------------------------#################################


#CRUD USER

#List
class UserListView(ListView):
    model = User
template_name = "base.html"

#Update
def user_update(request, user_cod):
    post = get_object_or_404(User, pk=user_cod)
    if request.method == "POST":
        form = UserForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False) 
            post.save()
            return redirect('/userlist')
    else:
        form = UserForm(instance=post)
    return render(request, 'core/user_create.html', {'form': form})
    

# Delete
def user_delete (request, user_cod):
     post = get_object_or_404 (User, pk = user_cod)
     post.delete ()
     return redirect ('/userlist')

def user_create(request):
    submitted = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():        
            cd = form.cleaned_data
             # assert False
            form.save()
            return HttpResponseRedirect('/userlist')
    else:
        form = UserForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'core/user_create.html', {'form': form, 'submitted': submitted})


###################################### FIM CRUD USUÁRIO USER ######################################
##############################-------------------------------#################################