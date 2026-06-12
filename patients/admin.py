from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "contact_number", "email", "created_by", "created_at")
    search_fields = ("name", "email", "contact_number")
    list_filter = ("gender", "created_at")
