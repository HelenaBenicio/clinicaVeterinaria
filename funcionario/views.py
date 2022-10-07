from django.shortcuts import render
from django.views.generic import ListView
from .models import Funcionario

class ListaFuncionarioView(ListView):
    model = Funcionario
    queryset = Funcionario.objects.all().order_by('nome_completo')