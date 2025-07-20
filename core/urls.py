from django.contrib import admin
from django.urls import path, include
from .view import index
urlpatterns = [
    path('', view=index, name="home"),
    path('admin/', admin.site.urls),
    path('api/', include('sangrah.api.urls',namespace='sangrah')),
    path('api-auth', include('rest_framework.urls')),
]
