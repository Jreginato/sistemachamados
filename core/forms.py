from django import forms
from .models import *


class DivisaoForm(forms.ModelForm):

    class Meta:
        model = Divisao
        #fields = ['nome', 'sigla',]
        fields = '__all__'
        #exclude = ('nome') #exemplo de retirada de campo


class SecaoForm(forms.ModelForm):

    class Meta:
        model = Secao
        #fields = ['nome', 'sigla',]
        fields = '__all__'
        #exclude = ('nome') #exemplo de retirada de campo


#16/10
class AssuntoDivisaoForm(forms.ModelForm):

    class Meta:
        model = AssuntoDivisao
        fields = '__all__'

class AssuntoSecaoForm(forms.ModelForm):

    class Meta:
        model = AssuntoSecao
        fields = '__all__'

class DivisaoSecaoForm(forms.ModelForm):

    class Meta:
        model = DivisaoSecao
        fields = '__all__'

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        widgets = {'user_senha': forms.PasswordInput()}      
 

class UserDivisaoForm(forms.ModelForm):

    class Meta:
        model = UserDivisao
        fields = '__all__'


class UserSecaoForm(forms.ModelForm):

    class Meta:
        model = UserSecao
        fields = '__all__'

