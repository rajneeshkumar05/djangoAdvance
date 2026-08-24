from django.shortcuts import render
from django.contrib import messages

def show_msg(request):
        messages.debug(request,'This is a debug message.')
        messages.info(request,'This is an info.')
        return render(request,'message.html')

# Create your views here.
