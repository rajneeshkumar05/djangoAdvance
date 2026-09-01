from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache 
from django.http import HttpResponse

def UserProfileList(request):
    # Check if the data is already cached
    user_profiles = cache.get('user_profiles')

    if not user_profiles:
        # If not cached, fetch from the database
        print("Cache miss: Fetching data from database")
        user_profiles = UserProfile.objects.all()
        # Cache the data for 15 minutes (900 seconds)
        cache.set('user_profiles', user_profiles, timeout=900)
    else:
        print("Data retrieved from cache")

    return render(request, 'user_profile_list.html', {'user_profiles': user_profiles})