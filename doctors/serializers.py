from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_contact_number(self, value):
        if not value.replace("+", "").replace("-", "").replace(" ", "").isdigit():
            raise serializers.ValidationError("Enter a valid contact number.")
        return value

    def validate_experience_years(self, value):
        if value < 0:
            raise serializers.ValidationError("Experience years cannot be negative.")
        return value
