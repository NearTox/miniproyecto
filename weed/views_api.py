from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, status, generics, viewsets
from django.shortcuts import get_object_or_404
from .serializer import WeedSerializer
from .models import Weed

class WeedListado(generics.ListCreateAPIView):
  queryset = Weed.objects.all()
  serializer_class = WeedSerializer
  #filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
  filter_fields = ('weed', 'longitud', 'latitud', 'fecha')


class WeedDetalleView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Weed.objects.all()
  serializer_class = WeedSerializer
  filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
  filter_fields = ('weed',)
  search_fields = ('fecha',)
