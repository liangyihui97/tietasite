from django.contrib import admin

# Register your models here.
from .models import Course, StationInfo, StationCodeInfo,zujin,dianfei

admin.site.register(Course)

admin.site.register(StationInfo)

admin.site.register(StationCodeInfo)

admin.site.register(zujin)

admin.site.register(dianfei)