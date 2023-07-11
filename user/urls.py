from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

user_app = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
]
