from django.shortcuts import render

from django import forms
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Animal
from django import forms
from animal.forms import AnimalForm

class ListaAnimalView(ListView):
    model = Animal
    queryset = Animal.objects.all().order_by('nome')

class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    success_url = ''


