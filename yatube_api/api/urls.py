from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls))
]
