from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html') # RENDERIZA template home.html 
# (mágica do Django -> Não esqueça de especificar em settings.py em APPS_INSTALLED 
# a app 'recipes' para o Django encontrar o template)

def sobre(request):
    return HttpResponse("Sobre")

def contato(request):
    return HttpResponse("Contato")
