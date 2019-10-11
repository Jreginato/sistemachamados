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

# Create
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

class UsuarioCreate(CreateView):
    model = User
    template_name = 'core/user_create.html'
    fields = '__all__'
    #fields = ['usuario',]
    #success_url = reverse_lazy('mysite:companies')

