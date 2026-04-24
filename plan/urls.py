from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add_task),
    path('complete/<int:id>/', views.complete_task),
]