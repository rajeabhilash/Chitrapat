from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializser(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_style': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', "password", 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    # pylint: disable=type: ignore
    def save(self): 
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error': 'Password does not match anna!'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already in use anna!'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        
        return account