from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST': #if someone fills out form , Post it
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:# if user exist
            login(request, user)
            messages.success(request,(f'hii {username} You are now logined'))
            return redirect('adminpage') #routes to 'home' on successful login
        elif user is not None:
            login(request, user)
            return redirect('userpage')
        else:
            messages.success(request,('Error logging in'))

            return redirect('login') #re routes to login page upon unsucessful login
    else:
        return render(request, 'login.html', {})


def adminpage(request):
    return render(request, 'admintemplates/adminpage.html')