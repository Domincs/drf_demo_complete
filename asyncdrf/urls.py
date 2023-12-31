from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from asyncdrf.user_serialiser import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('clients/', include('clients.urls')),
    path('admin/', admin.site.urls),
]
