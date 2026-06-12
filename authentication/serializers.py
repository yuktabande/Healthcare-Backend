from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    class Meta:
        model = User
        fields = ("id", "name", "email", "password", "password2")
        extra_kwargs = {"email": {"required": True}}

    # Map "name" -> first_name for the built-in User model
    name = serializers.CharField(source="first_name", required=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs.pop("password2"):
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        name = validated_data.pop("first_name", "")
        user = User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=name,
        )
        return user

    def to_representation(self, instance):
        tokens = RefreshToken.for_user(instance)
        return {
            "id": instance.id,
            "name": instance.first_name,
            "email": instance.email,
            "tokens": {
                "refresh": str(tokens),
                "access": str(tokens.access_token),
            },
        }
