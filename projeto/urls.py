
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


# HTTP REQUEST <-> HTTP RESPONSE
def sobre_view(request):
    return HttpResponse("Página Sobre")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', sobre_view),
]
