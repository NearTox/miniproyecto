from django import forms
from django.forms import ModelForm

class weedForm(forms.Form):
    latitud = forms.FloatField(label='Latitud')
    longitud = forms.FloatField(label='Longitud')
    weed = forms.BooleanField(label="Puedes fumar aqui?")
    comentario = forms.CharField(max_length = 50)