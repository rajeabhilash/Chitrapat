from django.contrib import admin
from django.urls import path, include
from .view import index
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )
urlpatterns = [
    path('', view=index, name="home"),
    path('admin/', admin.site.urls),
    path('api/', include('sangrah.api.urls', namespace='sangrah')),
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('account/', include('user_app.api.urls')),
]
