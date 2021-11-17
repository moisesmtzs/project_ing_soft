from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Materia(models.Model):
    nombre = models.TextField(max_length=30)
    clave = models.TextField(max_length=8)
    
    def __str__(self):
        return '{}'.format(self.nombre)

class Profesor(models.Model):
    idProfesor = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=50)
    correo = models.TextField(max_length=50)
    codigo = models.TextField(max_length=10)
    calificacion = models.SmallIntegerField()
    materia = models.ManyToManyField(Materia)

    def __str__(self):
        return '{}'.format(self.nombre)

class Alumno(models.Model):
    idAlumno = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=50)
    correo = models.EmailField()
    codigo = models.TextField(max_length=10)

    def __str__(self):
        return '{}'.format(self.nombre)

class Comentario(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.nombre)

