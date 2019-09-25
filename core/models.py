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
