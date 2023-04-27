from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def contato(request):
    return render(request, 'contato.html')


def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')
