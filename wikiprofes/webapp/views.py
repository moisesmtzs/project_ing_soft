from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Profesor
from .forms import ProfesorForm

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')
def buscar(request):
    return render(request,'buscar.html')

def iniciarSe(request):
    return render(request,'iniciarSesion.html')

def registrarse(request):
    return render(request,'registrarse.html')

def create_profesor(request):
    context = {
        'form' : ProfesorForm()
    }

    if request.method == 'POST':
        formulario = ProfesorForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Tu cuenta fue creada! Ahora puede iniciar sesión')
            return redirect('')
         
    return render(request, "profesor/create_profesor.html", context)