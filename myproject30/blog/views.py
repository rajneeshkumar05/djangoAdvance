from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_test_email(request):
    subject = "Welcome to my Blog"
    message = render_to_string('blog/email.html',{
        'username':'Kiki',
        'course':'Django lectures',
    })

    email = EmailMessage(
        subject,
        message,
        "rk5677283@gmail.com",
        ['nr485179@gmail.com']
    )

    email.content_subtype = 'html'
    email.send()
    return HttpResponse("<h2>email send</h2>")