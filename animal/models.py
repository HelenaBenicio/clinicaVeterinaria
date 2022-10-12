from django.db import models

class Animal(models.Model):
    nome_pet = models.CharField(max_length=256),
    data_de_nascimento = models.DateField(),
    idade = models.IntegerField(),
    especie = models.CharField(max_length=20),
    raca = models.CharField(max_length=20)