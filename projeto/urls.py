
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


# HTTP REQUEST <-> HTTP RESPONSE
def home(request):
    return HttpResponse("Home")

def sobre(request):
    return HttpResponse("Sobre")

def contato(request):
    return HttpResponse("Contato")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home), # Rota: / "apenas domínio raiz ou ip do servidor: http://127.0.0.1:8000/"
    path('sobre/', sobre), # Rota: /sobre/
    path('contato/', contato), # Rota: /contato/
]
