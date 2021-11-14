from django.contrib import admin
from .models import Profesor, Alumno, Comentario

# Register your models here.

admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Comentario)