from django.contrib import admin
from .models import Materia, Profesor, Alumno, Comentario

# Register your models here.

admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Comentario)
admin.site.register(Materia)
