from django.urls import path
from .views import MenuItemView


menu_app = 'menu'

urlpatterns = [
    path('', MenuItemView.as_view(), name='menu'),
]
