from django.conf.urls import url, include


urlpatterns = [
    url(r'^weed/', include("weed.urls_api")),
]
