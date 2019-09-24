from django.shortcuts import render
from django.http import HttpResponse #nova
# Create your views here.



def login(request):
    return render(request, 'login.html')

def inicio(request):
    return render(request, 'inicio.html')





