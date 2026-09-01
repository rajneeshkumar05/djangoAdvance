from . import views
from django.urls import path

urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('clear_cache/', views.clear_cache, name='clear_cache')
]