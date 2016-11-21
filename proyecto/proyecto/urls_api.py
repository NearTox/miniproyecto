from django.conf.urls import url, include
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token, verify_jwt_token)

urlpatterns = [
    url(r'^weed/', include("weed.urls_api")),
    
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
