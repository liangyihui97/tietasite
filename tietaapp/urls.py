#本地路由
from django.urls import path

from . import views #.代表当前app

# 加上 app_name 设置命名空间'tieta'，才能在{%url%}内通过别名访问
app_name = 'tieta'
urlpatterns = [
    path('', views.index, name='index'),
    path('stationinfo/', views.stationinfo, name='stationinfo'),
    path('stationcodeinfo/', views.stationcodeinfo, name='stationcodeinfo'),
    path('stationdetail/<int:id>/', views.stationdetail, name='stationdetail'),
    path('register/', views.RegView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('api/echarts/', views.echarts_data, name='apiecharts'),
    #path('map/', views.map, name='map'),
]

handler404 = views.view_404
handler500 = views.view_500