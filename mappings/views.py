from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import PatientDoctorMapping
from .serializers import MappingSerializer, MappingDetailSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MappingSerializer
        return MappingDetailSerializer

    def get_queryset(self):
        return PatientDoctorMapping.objects.select_related("patient", "doctor").all()


class MappingByPatientView(generics.ListAPIView):
    """GET /api/mappings/<patient_id>/ — all doctors for a given patient."""
    serializer_class = MappingDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient_id=self.kwargs["patient_id"]
        ).select_related("patient", "doctor")


class MappingDeleteView(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"detail": "Mapping removed successfully."}, status=status.HTTP_200_OK)
