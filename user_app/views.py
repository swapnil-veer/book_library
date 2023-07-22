from django.shortcuts import render, HttpResponse, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate , logout#add this
from django.contrib.auth.forms import AuthenticationForm #add this


# Create your views here.

def user_signup(request):
    if request.method == "POST":
        data = request.POST
        form = NewUserForm(data)
        if form.is_valid():
            user = form.save()
            print(user)
            messages.success(request,f"user : {user.username} saved successfully...!")
        else:
            messages.error(request, "Unsuccessful Signup, Data is Invalid....!")
        return redirect("user_login")
    elif request.method == "GET":
        form = NewUserForm()
        # print("in get request")
        return render(request=request,template_name='register.html',context={'signup_form': form})
    
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= user_name, password= password)
            if user:
                login(request,user)
                messages.success(request, "Logged in successfully...!")
                return redirect("home_page")
        else:
            messages.error(request,"Invalid credentials.!")
            return redirect("home_page")
    elif request.method == "GET":
        return render(request,"login.html",{'login_form':AuthenticationForm()})
    
def user_logout(request):
    logout(request)
    return redirect("user_login")
