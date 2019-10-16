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

    #CRUD SECAO
    path('secaolist/', SecaoListView.as_view(), name='secao_list'),
    path('secao_create/', views.secao_create, name='secao_create'), #nomedigitadourl/name é o nome do html
    path('secao_delete/<int:secao_codigo>', views.secao_delete, name='secao_delete'),
    path('secao/<int:secao_codigo>', views.secao_update, name='secao_update'),
    
    #16/10
    #CRUD USER
    path('userlist/',   UserListView.as_view(), name='user_list'),
    path('user_create/', views.user_create, name='user_create'), #nomedigitadourl/name é o nome do html
    path('user_delete/<int:user_cod>', views.user_delete, name='user_delete'),
    path('user/<int:user_cod>', views.user_update, name='user_update'),




] 


