
from django.db import models
from django.db.models.deletion import CASCADE

from webapp.managers import SoftDeleteManager

# Create your models here.

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeleteManager
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True

class Materia(SoftDeleteModel):
    clave = models.TextField(max_length=8)
    nombre = models.TextField(blank=True,max_length=50)
    horario = models.TextField(blank=True,max_length=30 )
    salon = models.TextField(blank=True,max_length=20)
    def __str__(self):
        return '{}'.format(self.clave)

class Profesor(SoftDeleteModel):
    idProfesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    codigo = models.CharField(max_length=10)
    #calificacion = models.SmallIntegerField()
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
    profesor = models.ForeignKey(Profesor,  on_delete= models.CASCADE)
    #alumno = models.ForeignKey(Alumno, on_delete=CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.profesor.nombre, self.fecha)

