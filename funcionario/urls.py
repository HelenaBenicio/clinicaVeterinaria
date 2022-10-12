from django.urls import path
from .views import ListaFuncionarioView, TriagemCreateView, ListaTriagemView

urlpatterns = [
    path('', ListaFuncionarioView.as_view(), name='funcionario.index'),
    path('triagem/', TriagemCreateView.as_view(), name='funcionario.triagem' ),
    path('triagem/lista-triagem', ListaTriagemView.as_view(), name='funcionario.listatriagem')
]