from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('add/', views.add_task),
    path('complete/<int:id>/', views.complete_task),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]