from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, LoginSerializer
from .models import User


@api_view(['POST'])
def signup_apiview(request):
    if request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_apiview(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        email = request.data['email']
        if serializer.is_valid():
            user = User.objects.get(email=email)
            token = Token.objects.get_or_create(user=user)
            return Response({'message': 'Login Successful.',
                            'token': str(token[0])}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'serializer.errors'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def logout(request):
    if request.method == 'GET':
        request.user.auth_token.delete()
        return Response({'message': 'Logged Out Successfully.'}, status=status.HTTP_200_OK)
