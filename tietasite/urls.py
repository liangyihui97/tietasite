"""tietasite URL Configuration
全局路由
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from tietaapp import views #某个具体的app，需要将本地路由于全局路由相关联


urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('tietaapp.urls')),#引用tietaapp的本地路由，tietaapp即为app的名字，这样可以方便即插即用，也可以通过url进行识别当前处于什么系统
]
