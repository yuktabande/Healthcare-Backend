from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization", "experience_years", "email", "available")
    search_fields = ("name", "email", "specialization")
    list_filter = ("specialization", "available")
