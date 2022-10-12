from pyexpat import model
import django
from .models import Animal
from django import forms
from django.forms import fields, models

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome_pet','data_de_nascimento','idade','raça','espécie']