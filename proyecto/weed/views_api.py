from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import WeedSerializer
from .models import Weed

class WeedListado(APIView):
  def get(self, request, format=None):
    listado = Weed.objects.all()
    serializer = WeedSerializer(listado, many = true)
    return Response(serializer.data)