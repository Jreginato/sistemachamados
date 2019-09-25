from django.shortcuts import render
from django.http import HttpResponse #nova
#25/09 - Tentando primeiro Crud
from .models import Divisao
from django.views.generic import ListView, CreateView, UpdateView, DeleteView



# Create your views here.



def login(request):
    return render(request, 'login.html')


def inicio(request):
    return render(request, 'inicio.html')

#def divisao(request):
    #return render(request, 'divisao.html')


class DivisaoListView(ListView):
    model = Divisao
template_name = "base.html"


class DivisaoCreateView(CreateView):
    model = Divisao
    template_name = "base.html"


class DivisaoUpdateView(UpdateView):
    model = Divisao
    template_name = "base.html"


class DivisaoDeleteView(DeleteView):
    model = Divisao
    template_name = "base.html"



