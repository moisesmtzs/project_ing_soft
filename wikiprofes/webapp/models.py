from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Profesor(models.Model):
    idProfesor = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=50)
    correo = models.TextField(max_length=50)
    codigo = models.TextField(max_length=10)
    calificacion = models.SmallIntegerField()
    materia = models.TextField(max_length=6)

class Alumno(models.Model):
    idAlumno = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=50)
    correo = models.TextField(max_length=50)
    codigo = models.TextField(max_length=10)

class Comentario(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)