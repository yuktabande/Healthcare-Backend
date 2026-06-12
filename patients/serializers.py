from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ("id", "created_by", "created_at", "updated_at")

    def validate_contact_number(self, value):
        if not value.replace("+", "").replace("-", "").replace(" ", "").isdigit():
            raise serializers.ValidationError("Enter a valid contact number.")
        return value
