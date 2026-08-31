from django.urls import path
from . import views

urlpatterns = [
    path('get-session/',views.get_session,name='get_session'),
    path('set-session/',views.set_session,name='set_session'),
    path('delete-session/',views.delete_all_session,name='delete_session'),
]