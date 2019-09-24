from django.urls import path
from . import views

#arquivo criado para citar coleção de urls

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('', views.login, name='login'),
]