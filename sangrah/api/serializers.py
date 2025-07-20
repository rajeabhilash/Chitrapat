from rest_framework import serializers
from sangrah.models import Content, StreamPlatform, Review
from django.db.models import Avg

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='sangrah:content-detail', read_only=True)
    class Meta:
        model = Content
        fields = '__all__'
        
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name = 'sangrah:content-detail'
    )
    no_of_content = serializers.SerializerMethodField(read_only=True)
    no_of_active_content = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'sangrah:stream-detail', 'lookup_field': 'pk'}
        }
        
    def get_no_of_content(self, obj):
        return obj.content.count()
    
    def get_no_of_active_content(self, obj):
        return obj.content.filter(active=True).count()
    
    