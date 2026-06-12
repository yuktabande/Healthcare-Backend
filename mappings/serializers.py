from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = "__all__"
        read_only_fields = ("id", "assigned_at")

    def validate(self, attrs):
        if PatientDoctorMapping.objects.filter(
            patient=attrs["patient"], doctor=attrs["doctor"]
        ).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )
        return attrs


class MappingDetailSerializer(serializers.ModelSerializer):
    """Nested serializer for read operations — returns full patient/doctor objects."""
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = "__all__"
        read_only_fields = ("id", "assigned_at")
