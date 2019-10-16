from django.db import models
from .validate import *

# Create your models here.
# unique evita duplicidades
# null permite nulo
# blank não permite campo em branco
# para transformar em maiusculo necessita criar o def save 

class Divisao(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250, blank=False, null=True, unique=True)
    sigla = models.CharField(max_length=30, blank=False, null=True, unique=True)

    class Meta:
        managed = False
        db_table = 'divisao'

    def save(self, force_insert=False, force_update=False):
        self.nome = self.nome.upper()
        self.sigla = self.sigla.upper()
        super(Divisao, self).save(force_insert, force_update)    

    def __str__(self):
        return self.nome
    #def get_absolute_url(self):
    # return reverse_lazy('divisao', kwargs={'pk': self.id})


class Secao(models.Model):
    secao_codigo = models.AutoField(primary_key=True)
    secao_nome = models.CharField(max_length=250, unique=True)
    secao_sigla = models.CharField(max_length=30, unique=True) 
    divisao_codigo = models.ForeignKey(Divisao, models.DO_NOTHING, db_column='divisao_codigo')

    class Meta:
        managed = False
        db_table = 'secao'
    # Para transformar em maiuscula
    def save(self, force_insert=False, force_update=False):
        self.secao_nome = self.secao_nome.upper()
        self.secao_sigla = self.secao_sigla.upper()
        super(Secao, self).save(force_insert, force_update)    
    def __str__(self):
        return self.secao_nome


#16/10

class AssuntoDivisao(models.Model):
    divisao_cod = models.ForeignKey('Divisao', models.DO_NOTHING, db_column='divisao_cod')
    assunto_nome = models.CharField(max_length=255, unique=True, blank=False)
    assunto_desc = models.TextField(blank=False)

    class Meta:
        managed = False
        db_table = 'assunto_divisao'

    def save(self, force_insert=False, force_update=False):
        self.assunto_nome = self.assunto_nome.upper()
        self.assunto_desc = self.assunto_desc.upper()
        super(AssuntoDivisao, self).save(force_insert, force_update)    
    def __str__(self):
        return self.assunto_nome


class AssuntoSecao(models.Model):
    secao_cod = models.ForeignKey('Secao', models.DO_NOTHING, db_column='secao_cod')
    assunto_nome = models.CharField(max_length=255, unique=True, blank=False)
    assunto_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'assunto_secao'
    
    def save(self, force_insert=False, force_update=False):
        self.assunto_nome = self.assunto_nome.upper()
        self.assunto_desc = self.assunto_desc.upper()
        super(AssuntoSecao, self).save(force_insert, force_update)    
    def __str__(self):
        return self.assunto_nome

class DivisaoSecao(models.Model):
    divisao_cod = models.ForeignKey(Divisao, models.DO_NOTHING, db_column='divisao_cod')
    secao_cod = models.ForeignKey('Secao', models.DO_NOTHING, db_column='secao_cod')

    class Meta:
        managed = False
        db_table = 'divisao_secao'

class User(models.Model):
    ATIVO_CHOICES=[("ATIVO","ATIVO"),("INATIVO","INATIVO")]
    BLOQUEADO_CHOICES=[("BLOQUEADO","BLOQUEADO"),("DESBLOQUEADO","DESBLOQUEADO")]
    

    user_cod = models.AutoField(primary_key=True)
    user_nome = models.CharField("Nome Completo",max_length=250, blank=False, null=False)
    user_email = models.EmailField("Email",unique=True, blank=False)
    user_ativo = models.CharField("Situação",max_length=25,choices=ATIVO_CHOICES, blank=False, null=False)
    user_bloqueado = models.CharField("Bloqueado?",max_length=25,choices=BLOQUEADO_CHOICES, blank=False, null=False)
    user_cpf = models.CharField("CPF",max_length=11, blank=False, null=False, unique=True, validators=[validate_CPF])
    user_senha = models.CharField("Senha",max_length=250, blank=False, null=False)
 
    
    class Meta:
        managed = False
        db_table = 'user'
    

    def save(self, force_insert=False, force_update=False):
        self.user_nome = self.user_nome.upper()
        self.user_email = self.user_email.upper()
        self.user_ativo = self.user_ativo.upper()
        self.user_bloqueado = self.user_bloqueado.upper()
        self.user_cpf = self.user_cpf.upper()
        self.user_senha = self.user_senha #possível erro

        super(User, self).save(force_insert, force_update)    
    def __str__(self):
        return self.user_nome

class UserDivisao(models.Model):
    user_cod = models.ForeignKey(User, models.DO_NOTHING, db_column='user_cod')
    divisao_cod = models.ForeignKey(Divisao, models.DO_NOTHING, db_column='divisao_cod')
    cargo = models.CharField(max_length=50, blank=False)

    class Meta:
        managed = False
        db_table = 'user_divisao'

    def save(self, force_insert=False, force_update=False):
        self.cargo = self.cargo.upper()
        super(UserDivisao, self).save(force_insert, force_update)    
    def __str__(self):
        return self.cargo

class UserSecao(models.Model):
    user_cod = models.ForeignKey(User, models.DO_NOTHING, db_column='user_cod')
    secao_cod = models.ForeignKey(Secao, models.DO_NOTHING, db_column='secao_cod')
    cargo = models.CharField(max_length=50, blank=False)

    class Meta:
        managed = False
        db_table = 'user_secao'

    def save(self, force_insert=False, force_update=False):
        self.cargo = self.cargo.upper()
        super(UserSecao, self).save(force_insert, force_update)    
    def __str__(self):
        return self.cargo
