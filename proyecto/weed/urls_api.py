from django.conf.urls import url, include
from .views_api import WeedListado, WeedDetalleView
urlpatterns =[
  url(r'^$', WeedListado.as_view()),
  url(r'^(?P<pk>[0-9]+)/$', WeedDetalleView.as_view()),
]