from django.shortcuts import render
from .models import *

def home(request):
    return render(request,'home.html')

def autos(request):
    datos = {
    'autos':Auto.objects.all()
    }
    return render(request,'autos.html',datos)

def clientes(request):
    datos = {
        'clientes':Cliente.objects.all()
    }
    return render(request,'clientes.html',datos)