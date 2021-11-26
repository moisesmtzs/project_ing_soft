from django import forms
from django.forms import fields
from .models import Profesor
from .models import Comentario

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor

        fields = ['nombre','correo','codigo','materia']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario

        fields = ['profesor','comentario']