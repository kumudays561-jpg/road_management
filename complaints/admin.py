from django.contrib import admin
from .models import Complaint
from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'assigned_engineer',
        'status'
    )
