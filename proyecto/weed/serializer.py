from rest_framework import serializers
from .models import Weed
class WeedSerializer(serializers.ModelSerializer):
  class Meta:
    model = Weed
    fields = ["id",
    "latitud",
      "longitud",
      "fecha",
      "weed",
      "comentario",
    ]
    #exlude = []

class WeedSerializerV2(serializers.ModelSerializer):
  class Meta:
    model = Weed
    exclude = []