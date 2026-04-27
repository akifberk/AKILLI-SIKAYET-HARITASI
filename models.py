from django.db import models


class Report(models.Model):
    class Category(models.TextChoices):
        ROAD = "road", "Yol Problemi"
        TRASH = "trash", "Cop / Temizlik"
        WATER = "water", "Su Kacagi"
        ELECTRIC = "electric", "Elektrik Arizasi"
        TRAFFIC = "traffic", "Trafik Sorunu"
        NOISE = "noise", "Gurultu Sikayeti"
        SECURITY = "security", "Guvenlik Sorunu"
        LIGHTING = "lighting", "Sokak Aydinlatmasi"
        PARK = "park", "Park / Bahce Sorunu"
        OTHER = "other", "Diger"

    class Status(models.TextChoices):
        PENDING = "pending", "Beklemede"
        RESOLVED = "resolved", "Cozuldu"

    category = models.CharField(max_length=20, choices=Category.choices)
    description = models.TextField()
    photo = models.ImageField(upload_to="reports/")
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.created_at:%d.%m.%Y %H:%M}"
