from django.shortcuts import render, redirect
from django.http import HttpResponse #nova
#25/09 - Tentando primeiro Crud
from .models import Divisao
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import DivisaoForm



# Create your views here.



def login(request):
    return render(request, 'login.html')


def inicio(request):
    return render(request, 'inicio.html')

#CREATE DIVISÃO
def divisao_create(request):
    form = DivisaoForm()    #<arquivo forms.py
    return render(request, "core/divisao_create.html", {'form':form})  # retornando html renderizado
#                           /\ sempre colocar o template do APP/ e o form .html


class DivisaoListView(ListView):
    model = Divisao
template_name = "base.html"


#class DivisaoCreateView(CreateView):
 #   model = Divisao
  #  form_class = DivisaoForm
   # template_name = "base.html"
    #sucess_url = reverse_lazy('divisao_list')


    #form_class = DivisaoForm

#def form_valid(self, form):
 #       print('form is valid')
  #      print(form.data)
   #     obj = form.save(commit=False)
    #    obj.save()
     #   return HttpResponseRedirect(reverse('divisao', kwargs={'pk': obj.id}))
  

class DivisaoUpdateView(UpdateView):
    model = Divisao
    template_name = "base.html"
    


class DivisaoDeleteView(DeleteView):
    model = Divisao
    template_name = "base.html"



