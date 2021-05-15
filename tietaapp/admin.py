from django.contrib import admin

# Register your models here.
from .models import Course, StationInfo, StationCodeInfo

admin.site.register(Course)

admin.site.register(StationInfo)

admin.site.register(StationCodeInfo)