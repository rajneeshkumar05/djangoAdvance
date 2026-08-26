from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

#REGIRSTER
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            user=form.save()
            login(request,user)
            messages.success(request,"Registeration successfully")
            return render('dashboard')
        else:
            messages.error(request,'Registration faild , try again')
    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

#LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfully')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username')
    return render(request,'accounts/login.html')

#LOGOUT
def logout_view(request):
    logout(request)
    messages.success(request,'logout successful')
    return redirect('login')

#DASHBOARD
@login_required(login_url='login')
def dashboard_view(request):
    return render(request,'accounts/dashboard.html')
    