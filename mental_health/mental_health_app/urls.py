from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns = [
	path('',views.index,name="index"),
	path('/doctors/',views.doctors, name='doctors')
]