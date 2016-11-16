from django.conf.urls import url, include
from .views_api import WeedListadoV2, WeedDetalleViewV2, WeedViewSet
'''
urlpatterns =[
  url(r'^$', WeedListadoV2.as_view()),
  url(r'^(?P<pk>[0-9]+)/$', WeedDetalleViewV2.as_view()),
]

weed_list = WeedViewSet.as_view({
  'get':'list',
  'post':'create'
})
weed_detail = WeedViewSet.as_view({
  'get':'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'
})

urlpatterns =[
  url(r'^$', weed_list),
  url(r'^(?P<pk>[0-9]+)/$', weed_detail),
]
'''
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'',WeedViewSet)

urlpatterns=[
  url(r'^',include(router.urls)),
]