from rest_framework import serializers
from sangrah.models import Movie

def name_length(value):
    if len(value)<2:
        raise serializers.ValidationError("Chota sa nam hai re!")
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
        # return super().create(validated_data)
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
        # return super().update(instance, validated_data)
    
    def validate(self, attrs):
        if attrs['name'] == attrs['description']:
            raise serializers.ValidationError("Name and Description should not match!")
        return attrs
        # return super().validate(attrs)
    
    # def validate_name(self, attrs):
    #     if len(attrs)<2:
    #         raise serializers.ValidationError("Chota sa nam hai re!")
    #     return attrs
        # return super().validate(attrs)