from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app.api.serializers import RegistrationSerializser

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"status":"logged out"}, status=status.HTTP_205_RESET_CONTENT)
    
    pass
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializser(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Susvagatam! - Registration Successful"
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
            
        else:
            data = serializer.errors
        return Response(data)