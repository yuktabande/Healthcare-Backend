from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    experience_years = models.PositiveIntegerField(default=0)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Dr. {self.name} — {self.specialization}"
