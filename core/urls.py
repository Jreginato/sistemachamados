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
    path('divisao/delete/<int:pk>', views.DivisaoDeleteView.as_view(), name='divisao_delete'),
    path('divisaolist/', DivisaoListView.as_view(), name='divisao_list'),
    path('divisao/<int:pk>', views.DivisaoUpdateView.as_view(), name='divisao_update'),

    #CRUD USER
    path('user_create/', UsuarioCreate.as_view(), name = 'user_create.html'),




] 


