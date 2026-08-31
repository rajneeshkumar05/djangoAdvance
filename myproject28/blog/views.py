from django.shortcuts import render
from django.http import HttpResponse


def set_session(request):
    request.session['username'] = 'kiki'
    request.session['course'] = 'Django full course'
    return HttpResponse("session data saved successfully")

def get_session(request):
    username = request.session.get('username','Guest')
    course = request.session.get('course','None')
    return HttpResponse(f"Welcome {username},You are learning{course}")

def delete_all_session(request):
    #try:
    #    del request.session['username']
    #except KeyError:
    #    return HttpResponse('Session key deleted')
    request.session.flush()
    return HttpResponse("All session deleted")