from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')
def buscar(request):
    return render(request,'buscar.html')

def iniciarSe(request):
    return render(request,'iniciarSesion.html')

def registrarse(request):
    return render(request,'registrarse.html')