from django.conf.urls import url, include
from .views_api import WeedListado
urlpatterns =[
  url(r'^weed/', WeedListado.as_view())
]