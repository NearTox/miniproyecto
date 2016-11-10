from django.db import models

# Create your models here.

class Weed(models.Model):
  #Atributes
  latitud = models.IntegerField(blank = True, null = False, default = 0)
  longitud = models.IntegerField(blank = True, null = False, default = 0)
  fecha = models.DateField(auto_now_add = True)
  weed = models.BooleanField(blank=True, null = False, default = False)
  comentario = models.CharField(max_lenght = 50, null = False, default = '')
