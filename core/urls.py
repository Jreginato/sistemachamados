from django.urls import path
from . import views
from .views import *

#arquivo criado para citar coleção de urls

urlpatterns = [
    #Links
    path('inicio/', views.inicio, name='inicio'),
    path('', views.login, name='login'),

    #CRUD DIVISAO
    path('divisao_create/', views.divisao_create, name='divisao_create'), #nomedigitadourl/name é o nome do html
    path('divisao_delete/<int:codigo>', views.divisao_delete, name='divisao_delete'),
    path('divisaolist/', DivisaoListView.as_view(), name='divisao_list'),
    path('divisao/<int:codigo>', views.divisao_update, name='divisao_update'),

    #CRUD USER
    path('user_create/', UsuarioCreate.as_view(), name = 'user_create.html'),




] 


