from django.shortcuts import render
from rest_framework import viewsets, serializers
from django.contrib.auth.models import User

MIN_LENGTH=8

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,

    )

    password2 = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,


    )

    class Meta:
        model=User
        fields="__all__"

    def validators(self, data):
        if data['password']!=data['password2']:
            raise serializers.ValidationError("not matching")
        return data

    def create(self, validated_data):
        user = User.object.create(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],

        )
        user.set_passowrd(validated_data["password"])
        user.save()
        return user

class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer

