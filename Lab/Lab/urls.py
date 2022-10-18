# Пути сайта
# Соответствие URL-ов обработчикам из Views

from django.contrib import admin
from django.urls import path
from BaumstagramLab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.Welcome),
    path('', views.GetPics),
    path('pic/<int:id>/', views.GetPic, name='pic_url'),
]
