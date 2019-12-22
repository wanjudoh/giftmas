from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.new, name='new'),
    path('detail/<int:letter_id>', views.detail, name='detail'),
    path('gift', views.gift, name='gift'),
]