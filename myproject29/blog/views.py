from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("cookies set successfully")
    response.set_cookie('username','Krish',60*60*24)
    response.set_cookie('course','django full course',60*60*24)
    return response

def get_cookie(request):
    username = request.COOKIES.get('username','Guest')
    course = request.COOKIES.get('course','Not enroled')
    if 'username' in request.COOKIES:
        return HttpResponse(f"Username: {username}, Course: {course}")
    else:
        return HttpResponse("No cookies found")

def delete_cookie(request):
    response = HttpResponse("cookies deleted successfully")
    response.delete_cookie('username')
    return response