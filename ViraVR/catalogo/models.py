from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class clasificacion(models.Model):
	nombre = models.CharField(max_length=200, default='NONE')
	descripcion = models.CharField(max_length=200, default='NONE')
	def __str__(self):
		return self.nombre

class especie(models.Model):
	nombre = models.CharField(max_length=200, default='NONE')
	clasificacion = models.ForeignKey(clasificacion, on_delete = models.CASCADE)
	familia = models.CharField(max_length = 200, default='NONE')
	nombre_cientifico = models.CharField(max_length = 200, default='NONE')
	comienzo_siembra = models.DateField(default=date.today)
	termino_siembra = models.DateField(default=date.today)
	distancia_entre_siembras = models.IntegerField(default = 0)
	altura = models.IntegerField(default=0)
	temperatura_de_germinacion = models.IntegerField(default=0)
	temperatura_de_crecimiento = models.IntegerField(default=0)
	ph = models.IntegerField(default=0)
	color = models.CharField(max_length=200, default='NONE')
	miembro_cosechable = models.CharField(max_length=200, choices = [(1, 'Hoja'),(2, 'Raiz'),(3, 'Flor'),(4, 'Bulbo'),], default='No especificada.')
	tamano = models.IntegerField(default=0)
	lugar_de_plantacion = models.CharField(max_length=200, choices = [(1, 'Interior'), (2, 'Exterior'), (3, 'Ambas'), ], default='No especificada.')
	descripcion_de_flor = models.CharField(max_length=200, default='NONE')
	requerimientos_de_suelo = models.CharField(max_length=200, default='NONE')
	requerimientos_de_riego = models.CharField(max_length=200, default='NONE')
	descripcion_de_fruto = models.CharField(max_length=200, default='NONE')
	def __str__(self):
		return self.nombre

class planta(models.Model):
	cod = models.AutoField(primary_key=True)
	usuario = models.ForeignKey(User)
	especie = models.ForeignKey(especie, on_delete = models.CASCADE)
	fecha_de_plantacion = models.DateField(default=date.today)
	def __str__(self):
		return self.nombre
