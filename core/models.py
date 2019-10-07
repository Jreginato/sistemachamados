from django.db import models

# Create your models here.

class Divisao(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    sigla = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'divisao'

    def __str__(self):
        return self.nome
    #def get_absolute_url(self):
    # return reverse_lazy('divisao', kwargs={'pk': self.id})

class User(models.Model):
    usuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    email = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(max_length=30)
    reg_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
     return self.usuario
