from winreg import CreateKey
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from clinicaVeterinaria.funcionario.forms import TriagemForm
from .models import Funcionario, Triagem

class ListaFuncionarioView(ListView):
    model = Funcionario
    queryset = Funcionario.objects.all().order_by('nome_completo')

class ListaTriagemView(ListView):
    model = Funcionario
    queryset = Triagem.objects.all().order_by('nome_pet')

class TriagemCreateView(CreateView):
    model = Triagem
    form_class = TriagemForm