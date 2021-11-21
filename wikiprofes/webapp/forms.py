from django import forms
from django.forms import fields
from .models import Profesor

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor

        fields = ['nombre','correo','codigo','materia']