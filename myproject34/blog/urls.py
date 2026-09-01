from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfileList, name='user_profile_list'),
]