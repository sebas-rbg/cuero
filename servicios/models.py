from django.db import models

# Create your models here.

class servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    def _str_(self):
        return self.titulo
