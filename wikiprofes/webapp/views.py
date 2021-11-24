from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

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
            messages.success(request, f'Profesor agregado con exito')
            return redirect('read_profesor')  #Cambiar a vista del menu CRUD   
         
    return render(request, "profesor/create_profesor.html", context)

def read_profesor(request):
    profesor = Profesor.objects.all()

    context = {
        'profesor': profesor
    }
    return render(request, "profesor/read_profesor.html", context)

def update_profesor(request, id):
    
    profesor = get_object_or_404(Profesor, idProfesor=id)

    context = {
        'form' : ProfesorForm(instance=profesor)
    }
    
    if request.method == 'POST':
        formulario = ProfesorForm(data=request.POST, instance=profesor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Datos modificados con exito')
            return redirect('read_profesor')
        context['form'] = formulario

    return render(request, 'profesor/update_profesor.html',context)

def delete_profesor(request, id):
    profesor = get_object_or_404(Profesor, idProfesor=id)
    profesor.delete()
    messages.success(request, f'Registro eliminado con exito')
    return redirect('read_profesor')

def search_profesor(request):
    if request.method == "POST":
        searched = request.POST['searched']
        profesor = Profesor.objects.filter(nombre__contains=searched)

        return render(request, 'profesor/search_profesor.html',{'searched':searched, 'profesor':profesor})
    else:
        return render(request, 'profesor/search_profesor.html',{})