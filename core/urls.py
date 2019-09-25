from django.urls import path
from . import views
from .views import DivisaoCreateView, DivisaoDeleteView, DivisaoListView, DivisaoUpdateView

#arquivo criado para citar coleção de urls

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    #path('divisao/', views.divisao, name='divisao'),
    path('', views.login, name='login'),
    path('divisaolist/', DivisaoListView.as_view(), name='divisao_list'), #nomedigitadourl   / name é o nome da view
]
    #path('divisao/', views.divisao, name='divisao'),
    #path('divisao/', views.divisao, name='divisao'),
    #path('divisao/', views.divisao, name='divisao'),

    