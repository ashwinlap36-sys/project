from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),   # 👈 first page = login
    path('home/', views.home, name='home'),     # 👈 move home to /home/
    path('add/', views.add_task),
    path('complete/<int:id>/', views.complete_task),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]