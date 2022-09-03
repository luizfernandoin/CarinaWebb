from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import json
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name: str = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        req = requests.get(f"https://api.nasa.gov/planetary/apod?api_key=AtfiXpPGoL0GQiirY3LmfEjJfB56JSDam3c34DOL")
        dados = json.loads(req.text)

        context["dados"] = { 
            "url" : dados["url"],
            "titulo" : dados["title"] 
            } 
            
        return context

class SobreView(TemplateView):
    template_name:str = "sobre.html"

class ContatoView(TemplateView):
    template_name: str = "contato.html"

class GaleriaView(LoginRequiredMixin, TemplateView):
    login_url = "../accounts/login/"
    template_name: str = "galeria.html"