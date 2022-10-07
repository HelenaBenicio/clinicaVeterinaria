from django.urls import path
from .views import ListaFuncionarioView

urlpatterns = [
    path('', ListaFuncionarioView.as_view(), name='funcionario.index')
]