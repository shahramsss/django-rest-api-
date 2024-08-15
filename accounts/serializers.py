from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email(value):
    if "admin" in value:
        raise serializers.ValidationError("admin cant in email")


class UserRegistrSerialiser(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError("user name cant be admin")
        return value

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("passwords not match")
        return data


class UserRegistrModelSerialiser(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"validators": (clean_email,)},
        }

    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError("user name cant be admin")
        return value

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("passwords not match")
        return data
