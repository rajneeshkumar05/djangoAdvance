from django.shortcuts import render
from .models import UserList
from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


#@cache_page(30)  # Cache the view for 30 seconds
def users_list(request):
    print("Fetching user list from database")
    users = UserList.objects.all()
    return render(request, 'users_list.html', {'users': users})

def clear_cache(request):
    cache.clear()
    return HttpResponse("Cache cleared.")