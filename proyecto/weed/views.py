from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Weed
# Create your views here.

class GetWeed(View):
  def get(sel, resquet,*args,**kargs):
    return render()

class NewWeed(View):
  def post(sel, resquet,*args,**kargs):