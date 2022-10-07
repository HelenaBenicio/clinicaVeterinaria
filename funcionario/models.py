import email
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=256),
    idade = models.IntegerField(),
    data_de_nascimento = models.DateField()
    cpf = models.IntegerField(unique=True)
    rg = models.IntegerField(unique=True)
    telefone = models.CharField(max_length=256)
    email = models.CharField(max_lengh=256)