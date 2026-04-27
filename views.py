from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render

from .forms import ReportForm
from .models import Report


CATEGORY_COLORS = {
    Report.Category.ROAD: "red",
    Report.Category.TRASH: "green",
    Report.Category.WATER: "blue",
    Report.Category.ELECTRIC: "orange",
    Report.Category.TRAFFIC: "yellow",
    Report.Category.NOISE: "pink",
    Report.Category.SECURITY: "purple",
    Report.Category.LIGHTING: "gold",
    Report.Category.PARK: "teal",
    Report.Category.OTHER: "gray",
}


def report_create(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("report_create")
    else:
        form = ReportForm()

    return render(request, "report.html", {"form": form})


@staff_member_required
def admin_map(request):
    reports = Report.objects.order_by("-created_at")
    report_data = [
        {
            "id": report.id,
            "category": report.get_category_display(),
            "description": report.description,
            "lat": report.latitude,
            "lng": report.longitude,
            "photo_url": report.photo.url if report.photo else "",
            "color": CATEGORY_COLORS.get(report.category, "gray"),
            "status": report.get_status_display(),
        }
        for report in reports
    ]
    return render(request, "admin_map.html", {"report_data": report_data})
