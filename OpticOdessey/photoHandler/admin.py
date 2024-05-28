from django.contrib import admin
from .models import *
# Register your models here.

class UploadImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at')

class ProcessedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at')

admin.site.register(UploadImage, UploadImageAdmin)
admin.site.register(ProcessedImage, ProcessedImageAdmin)
