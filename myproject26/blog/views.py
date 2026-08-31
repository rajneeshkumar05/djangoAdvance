from django.http import HttpResponse

def home_view(request):
    return HttpResponse("welcome to page")