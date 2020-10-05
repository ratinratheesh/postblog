from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def save(self, **kwargs):
        user = User(
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credentials, Please enter valid details.')
        if not user.is_active:
            raise AuthenticationFailed('Your account is inactive, Please contact admin.')
        return user