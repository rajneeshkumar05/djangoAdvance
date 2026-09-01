from django.core.cache import cache
from .models import YouTubeUser
from django.shortcuts import render

def users_list(request):
    users = cache.get('users_data')
    if not users:
        print("Cache miss: Fetching data from database")
        users = YouTubeUser.objects.all()
        cache.set('users_data', users, timeout=60*15)  # Cache for 15 minutes
    else:
        print("Data retrieved from cache")

    return render(request, 'youtube/users_list.html', {'users': users})
