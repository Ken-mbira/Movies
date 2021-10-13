from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

def login_user(request):
    """This will handle the user registration

    Args:
        request ([type]): [description]
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password = password)

        if user is not None:
            login(request,user)
            return redirect('index')

        else:
            messages.success(request,'You have entered invalid credentials, please check them and try again')
            return render(request,'authenticate/login.html')

    else:
        return render(request,'authenticate/login.html')
