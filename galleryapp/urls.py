from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView, name="home"),
    path('school/', views.school_list, name="school_list"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('add_school/', views.add_school, name="add_school"),
]