from django.urls import path

from . import views

app_name = "gymapp"
urlpatterns = [
    path('', views.homeview, name="home"),
]
