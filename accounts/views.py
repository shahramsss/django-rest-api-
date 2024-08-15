from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegistrSerialiser , UserRegistrModelSerialiser
from rest_framework import status 


class UserRegister(APIView):
    def post(self, request):
        # ser_data = UserRegistrSerialiser(data=request.POST)
        ser_data = UserRegistrModelSerialiser(data=request.POST)
        if ser_data.is_valid():
            # User.objects.create(
            #     username=ser_data.validated_data["username"],
            #     email=ser_data.validated_data["email"],
            #     password=ser_data.validated_data["password"],
            # )

            ser_data.create(ser_data.validated_data)
            return Response(data=ser_data.data , status=status.HTTP_201_CREATED)
        return Response(ser_data.errors , status=status.HTTP_400_BAD_REQUEST)
