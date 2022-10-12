from importlib.resources import path
from .views import AnimalCreateView

urlpatterns = [
    path('novo-animal/', AnimalCreateView.as_view(), name='animal.novo')
]
