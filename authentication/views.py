from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

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
            messages.success(request,f'Congratulations {username}, you were logged in successfully!')
            return redirect('index')

        else:
            messages.success(request,'You have entered invalid credentials, please check them and try again')
            return render(request,'authenticate/login.html')

    else:
        return render(request,'authenticate/login.html')

def logout_user(request):
    """This will logout a user

    Args:
        request ([type]): [description]
    """
    logout(request)
    messages.success(request,"You were logged out successfully")
    return redirect('index')

def register_user(request):
    """This will manage the proccesses involved in registering a new user

    Args:
        request ([type]): [description]
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,f"Congratulations {username}, you were successfully registered into Movie Galore")
            return redirect('index')

    else:
        form = UserCreationForm()
    return render(request,'authenticate/register_user.html',{'form':form})
        