#from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Weed(models.Model):
  #Atributes
  geoLoc = models.PointField()
  #latitud = models.IntegerField(blank = True, null = False, default = 0)
  #longitud = models.IntegerField(blank = True, null = False, default = 0)
  fecha = models.DateField(auto_now_add = True)
  weed = models.BooleanField(blank = True, null = False, default = False)
  comentario = models.CharField(max_length = 50, null = False, default = '')

  def __str__(self):
    return self.comentario
