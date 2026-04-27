from django import forms

from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["photo", "description", "category", "latitude", "longitude"]
        widgets = {
            "description": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Sorunu detayli sekilde yazin..."}
            ),
            "category": forms.Select(),
            "latitude": forms.HiddenInput(),
            "longitude": forms.HiddenInput(),
        }
