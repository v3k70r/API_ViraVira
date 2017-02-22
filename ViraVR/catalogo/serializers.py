from rest_framework import serializers
from .models import clasificacion, especie

class especieSerializers(serializers.Serializer):
	nombre = serializers.CharField(max_length=200)
	clasificacion = serializers.PrimaryKeyRelatedField(queryset=clasificacion.objects.all())
	tamano = serializers.IntegerField(default=0)
	lugar_de_plantacion = serializers.ChoiceField( choices = [(1, 'Interior'),(2, 'Exterior'),(3, 'Ambas')], default='No_especificada')
	def __str__(self):
		return self.nombre

class clasificacionSerializers(serializers.Serializer):
	nombre = serializers.CharField(max_length=200)
	descripcion = serializers.CharField(max_length=200)
	def __str__(self):
		return self.nombre