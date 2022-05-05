from django.contrib.auth import authenticate
from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'sex', 'birth_date', 'height', 'weight', 'goal', 'activity')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'sex', 'birth_date', 'height', 'weight', 'goal', 'activity', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['first_name'],
                                        validated_data['sex'], validated_data['birth_date'],
                                        validated_data['height'], validated_data['weight'],
                                        validated_data['goal'], validated_data['activity'],
                                        validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверный логин или пароль')