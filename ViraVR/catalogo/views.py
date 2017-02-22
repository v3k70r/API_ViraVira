from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from catalogo.models import especie, clasificacion
from catalogo.serializers import especieSerializers, clasificacionSerializers

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
    	content = JSONRenderer().render(data)
    	kwargs['content_type'] = 'application/json'
    	super(JSONResponse, self).__init__(content, **kwargs)

def especie_list(request):
  	if request.method == 'GET':
   		Especie = especie.objects.all()
   		serializer = especieSerializers(Especie, many=True)
   		return JSONResponse(serializer.data)
   	elif request.method == 'POST':
   		data = JSONParser().parse(request)
   		serializer = especieSerializers(data=data)
   		if serializer.is_valid():
   			serializer.save()
   			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

def especie_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Especie = especie.objects.get(pk=pk)
    except Especie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = especieSerializers(Especie)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = especieSerializer(Especie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Especie.delete()
        return HttpResponse(status=204)

def especie_detail_nombre(request, nombre):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Especie = especie.objects.get(nombre=nombre)
    except Especie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = especieSerializers(Especie)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = especieSerializer(Especie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Especie.delete()
        return HttpResponse(status=204)

def clasificacion_list(request):
  	if request.method == 'GET':
   		Clasificacion = clasificacion.objects.all()
   		serializer = clasificacionSerializers(Clasificacion, many=True)
   		return JSONResponse(serializer.data)
   	elif request.method == 'POST':
   		data = JSONParser().parse(request)
   		serializer = clasificacionSerializers(data=data)
   		if serializer.is_valid():
   			serializer.save()
   			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

def clasificacion_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Clasificacion = clasificacion.objects.get(pk=pk)
    except Clasificacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = clasificacionSerializers(Clasificacion)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = clasificacionSerializer(Clasificacion, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Clasificacion.delete()
        return HttpResponse(status=204)