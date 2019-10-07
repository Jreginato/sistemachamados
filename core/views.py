from django.shortcuts import render, redirect
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

#CREATE DIVISÃO
#def divisao_create(request): #Linha 01 correta
#    form = DivisaoForm() #linha 02 correta
#    return render(request, "core/divisao_create.html", {'form':form})  # Linha 03 correta retornando html renderizado
#                           /\ sempre colocar o template do APP/ e o form .html

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

def clean(self, *args, **kwargs):
    data = self.data
    cleaned = self.cleaned_data


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


class UsuarioCreate(CreateView):
    model = User
    template_name = 'core/user_create.html'
    fields = '__all__'
    #fields = ['usuario',]
    #success_url = reverse_lazy('mysite:companies')

