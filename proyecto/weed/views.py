from django.shortcuts import render, redirect
#from django.contrib.gis.geos import GEOSGeometry
from django.views.generic import View
from .models import Weed
from .forms import weedForm
# Create your views here.

class WeedView(View):
  form = weedForm()
  template = "weed.html"

  def get(self, request, *args, **kargs):
    return render(request, self.template,{"form":self.form})

  def post(self, request, *args, **kargs):
    self.form = weedForm(request.POST)

    if self.form.is_valid():
      weed = Weed() 
      weed.comentario = self.form.cleaned_data["comentario"]
      weed.latitud= self.form.cleaned_data["latitud"]
      weed.longitud= self.form.cleaned_data["longitud"]
      #weed.coods = GEOSGeometry("POINT({0} {1})".format(self.form.cleaned_data["latitud"],self.form.cleaned_data["longitud"]))
      weed.save()
      return redirect("weed-list")
    
    return redirect("weed-post")
