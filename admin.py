from django.contrib import admin

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "status", "created_at")
    list_filter = ("category", "status")
    search_fields = ("description",)
