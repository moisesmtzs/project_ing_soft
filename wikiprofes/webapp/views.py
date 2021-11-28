from django.db.models import fields
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Comentario, Profesor, Comentario
from .forms import CommentForm, ProfesorForm

# Create your views here.
def inicio(request):
    profesor = Profesor.objects.all()

    context = {
        'profesor': profesor
    }
    return render(request, 'inicio.html', context)
   
def buscar(request):
    return render(request,'buscar.html')

def iniciarSe(request):
    return render(request,'iniciarSesion.html')

def registrarse(request):
    return render(request,'registrarse.html')

def profesor_profile(request, id):
    profesor = get_object_or_404(Profesor, idProfesor=id)
    context = {
        'profesor': profesor
    }
    # return redirect('profesor/profesor_profile.html')
    return render(request, 'profesor/profesor_profile.html', context)

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

def AddCommentView(request):
    profesor = get_object_or_404(Profesor, idProfesor=id)

    context = {
        'profesor': profesor,
        'comment' : CommentForm()
    }

    if request.method == 'POST':
        formulario = CommentForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Comentario agregado con éxito')
            return redirect('profesor_profile')  #Cambiar a vista del menu CRUD   
         
    return render(request, "profesor/add_comment.html", context)
    # model = Comentario
    # template_name = 'add_comment.html'
    # fields = '__all__'