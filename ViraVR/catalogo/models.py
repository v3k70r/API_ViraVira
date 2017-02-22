from __future__ import unicode_literals

from django.db import models

class clasificacion(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

class especie(models.Model):
	clasificacion = models.ForeignKey(clasificacion, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200, unique = True)
	tamano = models.IntegerField(default=0)
	lugar_de_plantacion=models.CharField(max_length=200, choices = [(1, 'Interior'), (2, 'Exterior'), (3, 'Ambas'), ])
	def __str__(self):
		return self.nombre