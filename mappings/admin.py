from django.contrib import admin
from .models import PatientDoctorMapping

@admin.register(PatientDoctorMapping)
class MappingAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "assigned_at")
    search_fields = ("patient__name", "doctor__name")
