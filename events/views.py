from django.shortcuts import render
from rest_framework import viewsets

from . import models
from . import serializers

# Create your views here.
class EventosViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.EventoSerializer
	queryset = models.Evento.objects.all()