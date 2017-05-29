from rest_framework import serializers
from catalogo.models import clasificacion, especie
from django.contrib.auth.models import User
from datetime import date

class especieSerializers(serializers.Serializer):
	nombre = serializers.CharField(max_length=200, default='NONE')
	clasificacion = serializers.PrimaryKeyRelatedField(queryset=clasificacion.objects.all())
	familia = serializers.CharField(max_length=200, default='NONE')
	nombre_cientifico = serializers.CharField(max_length=200, default='NONE')
	comienzo_siembra = serializers.DateTimeField(default=date.today)
	termino_siembra = serializers.DateTimeField(default=date.today)
	distancia_entre_siembras = serializers.IntegerField(default=0)
	altura = serializers.IntegerField(default=0)
	temperatura_de_germinacion = serializers.IntegerField(default=0)
	temperatura_de_crecimiento = serializers.IntegerField(default=0)
	ph = serializers.IntegerField(default=0)
	color = serializers.CharField(max_length=200, default='NONE')
	miembro_cosechable = serializers.ChoiceField( choices = [(1, 'Hoja'),(2, 'Raiz'),(3, 'Flor'),(4, 'Bulbo'),], default='No especificada.')
	tamano = serializers.IntegerField(default=0)
	lugar_de_plantacion = serializers.ChoiceField( choices = [(1, 'Interior'),(2, 'Exterior'),(3, 'Ambas')], default='No especificada.')
	descripcion = serializers.CharField(max_length=200, default='NONE')
	descripcion_de_flor = serializers.CharField(max_length=200, default='NONE')
	requerimientos_de_suelo = serializers.CharField(max_length=200, default='NONE')
	requerimientos_de_riego = serializers.CharField(max_length=200, default='NONE')
	descripcion_de_fruto = serializers.CharField(max_length=200, default='NONE')
	def __str__(self):
		return self.nombre

class clasificacionSerializers(serializers.Serializer):
	nombre = serializers.CharField(max_length=200, default='NONE')
	descripcion = serializers.CharField(max_length=200, default='NONE')
	def __str__(self):
		return self.nombre

class plantaSerializers(serializers.Serializer):
	cod = serializers.ReadOnlyField()
	usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
	especie = serializers.PrimaryKeyRelatedField(queryset=especie.objects.all())
	fecha_de_plantacion = serializers.DateTimeField(default=date.today)
	def __str__(self):
		return self.nombre