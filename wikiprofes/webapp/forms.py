from django import forms
from django.forms import fields
from .models import Calificacion, Profesor
from .models import Comentario

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor

        fields = ['nombre','correo','codigo','materia']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario

        fields = ['profesor','comentario']

class CalifForm(forms.ModelForm):
    
    puntualidad = forms.IntegerField(max_value=10, min_value=0, label="Puntualidad")
    dificultad = forms.IntegerField(max_value=10, min_value=0, label="Dificultad")
    dominioDelTema = forms.IntegerField(max_value=10, min_value=0, label="Dominio del tema")
    facilidad = forms.IntegerField(max_value=10, min_value=0, label="Facilidad del curso")
    
    class Meta:
        model = Calificacion

        fields = ['puntualidad','dificultad','dominioDelTema','facilidad']