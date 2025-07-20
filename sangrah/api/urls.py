from django.urls import path
from sangrah.api.views import *

app_name = "sangrah"

urlpatterns = [
    path(route='', view=index, name="home"), # type: ignore
   
    path(route='content/', view=ContentListAPIView.as_view(), name="content-list"), # type: ignore
    path(route='content/<int:pk>', view=ContentDetailAPIView.as_view(), name="content-detail"), # type: ignore
   
    path(route='stream/', view=StreamPlatformListAPIView.as_view(), name="stream-list"), # type: ignore
    path(route='stream/<int:pk>', view=StreamPlatformDetailAPIView.as_view(), name="stream-detail"), # type: ignore
    
    # path(route='review/', view=ReviewList.as_view(), name="review-list"), # type: ignore
    # path(route='review/<int:pk>', view=ReviewDetail.as_view(), name="review-detail"), # type: ignore
    
    path(route='content/<int:pk>/review-create/', view=ReviewCreate.as_view(), name="review-create"), # type: ignore
    path(route='content/<int:pk>/review/', view=ReviewList.as_view(), name="review-list"), # type: ignore
    path(route='content/review/<int:pk>', view=ReviewDetail.as_view(), name="review-detail"), # type: ignore
]
