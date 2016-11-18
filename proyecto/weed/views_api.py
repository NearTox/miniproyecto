from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializer import WeedSerializer
from .models import Weed

class WeedListado(APIView):
  def get(self, request, format=None):
    listado = Weed.objects.all()
    serializer = WeedSerializer(listado, many = True)
    return Response(serializer.data)

  def post(self, request, format=None):
    weed = WeedSerializer(data = request.data)

    if weed.is_valid():
      weed.save()
      return Response(weed.data,status=status.HTTP_201_CREATED)
    return Response(weed.data,status=status.HTTP_400_BAD_REQUEST)

class WeedDetalleView(APIView):
  def get(self, request, pk, format=None):
    weed = get_object_or_404(Weed,pk=pk)
    serialize = WeedSerializer(weed)
    return Response(serialize.data)
    
  def put(self, request, pk, format=None):
    weed = get_object_or_404(Weed, pk=pk)
    serializer = WeedSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    weed = get_object_or_404(Weed, pk=pk)
    weed.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
from rest_framework import generics
from .serializer import WeedSerializerV2

class WeedListadoV2(generics.ListCreateAPIView):
  queryset = Weed.objects.all()
  serializer_class = WeedSerializerV2


class WeedDetalleViewV2(generics.RetrieveUpdateDestroyAPIView):
  queryset = Weed.objects.all()
  serializer_class = WeedSerializerV2
  filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
  filter_fields = ('weed',)
  search_fields = ('fecha',)


class WeedViewSet(viewsets.ModelViewSet):
  queryset = Weed.objects.all()
  serializer_class = WeedSerializerV2
  filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
  filter_fields = ('weed',)
  search_fields = ('fecha',)
