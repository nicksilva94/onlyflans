from django.shortcuts import render
from .models import Flan, ContactForm
from .forms import ContactFormForm
from django.http import HttpResponseRedirect

flanes = Flan.objects.all()
flanes_privados = Flan.objects.filter(is_private=True)
flanes_publicos = Flan.objects.filter(is_private=False)
contacto = ContactForm.objects

def indice(request):
    return render(request, 'index.html', {'flanes_publicos': flanes_publicos})


def acerca(request):
    return render(request, 'about.html', {})


def bienvenido(request):
    return render(request, 'welcome.html', {'flanes_privados': flanes_privados})
# Create your views here.

def contacto(request):

    if request.method == 'POST':

        form = ContactFormForm(request.POST)

        if form.is_valid():

            contact_form = ContactForm.objects.create(**form.cleaned_data)

            return HttpResponseRedirect('/exito')
    
    else:
        form = ContactFormForm()

    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})