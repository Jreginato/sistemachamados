from django import forms
from .models import *


class DivisaoForm(forms.ModelForm):

    class Meta:
        model = Divisao
        #fields = ['nome', 'sigla',]
        fields = '__all__'
        #exclude = ('nome') #exemplo de retirada de campo



