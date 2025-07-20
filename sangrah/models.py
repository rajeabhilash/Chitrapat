from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Content(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='content')
    avg_rating = models.FloatField(default=0)
    number_of_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE,related_name='review')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return str(self.rating)+ " | "+ self.content.title
    