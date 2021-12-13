from django.db import models
from django.db.models.base import Model

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Título')
    descripcion = models.TextField(verbose_name = 'Descripción')
    image = models.ImageField(verbose_name = 'Imagen', upload_to = "projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Ultima Edición')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ["-created"]
    def __str__(self):
        return self.title