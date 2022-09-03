from django.urls import path, include
from .views import HomeView, SobreView, ContatoView, GaleriaView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('contato/', ContatoView.as_view(), name="contato"),
    path('galeria/', GaleriaView.as_view(), name="galeria"),
]