from .models import Triagem
from django import forms
from django.forms import fields, models

class TriagemForm(forms.ModelForm):
    class Meta:
        model = Triagem
        fields = ['nome_pet','sintomas']