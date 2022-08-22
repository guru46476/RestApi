from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('add/',views.addPage),
    path('update/<int:ID>/',views.updateRecord),
    path('delete/<int:num>/',views.deleteRecord),
    path('api/',views.api),
]
