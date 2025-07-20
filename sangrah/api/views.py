from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from sangrah.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from sangrah.models import Content,StreamPlatform, Review
from sangrah.api.serializers import (ContentSerializer,
                                     StreamPlatformSerializer, 
                                     ReviewSerializer)

def index(reqeust):
    return HttpResponse("<h1>Content API Center!</h1>")

class ReviewList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ReviewSerializer
    
    def get_queryset(self): # type: ignore
        pk = self.kwargs['pk']
        return Review.objects.filter(content=pk)

class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    
    def get_queryset(self): # type: ignore
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        content = Content.objects.get(pk=pk)
        
        reviewer = self.request.user
        review_queryset = Review.objects.filter(content=content, reviewer=reviewer)
        
        if review_queryset.exists():
            raise ValidationError("You've already reviewd this content!")
        
        if content.number_of_rating == 0:
            content.avg_rating = serializer.validated_data['rating']
        else:
            content.avg_rating = (content.avg_rating + serializer.validated_data['rating']) /2 
        
        content.number_of_rating = content.number_of_rating + 1
        content.save()
        
        serializer.save(content=content, reviewer = reviewer)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    
class StreamPlatformListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all().order_by('id')
    serializer_class = StreamPlatformSerializer
     
class StreamPlatformDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all().order_by('id')
    serializer_class = StreamPlatformSerializer
    
class ContentListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Content.objects.all().order_by('id')
    serializer_class = ContentSerializer
   
class ContentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Content.objects.all().order_by('id')
    serializer_class = ContentSerializer