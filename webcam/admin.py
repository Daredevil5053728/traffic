from django.contrib import admin
from webcam.models import two_weeler
# Register your models here.

@admin.register(two_weeler)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "file"]
    readonly_fields = ["date_added"]