from django.shortcuts import render
from .models import Flan

flanes = Flan.objects.all()
flanes_privados = Flan.objects.filter(is_private=True)
flanes_publicos = Flan.objects.filter(is_private=False)

def indice(request):
    return render(request, 'index.html', {'flanes_publicos': flanes_publicos})


def acerca(request):
    return render(request, 'about.html', {})


def bienvenido(request):
    return render(request, 'welcome.html', {'flanes_privados': flanes_privados})
# Create your views here.
