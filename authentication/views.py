from django.shortcuts import render

def login_user(request):
    """This will handle the user registration

    Args:
        request ([type]): [description]
    """
    message = 'Hello world!'
    return render(request,'authenticate/login.html',{"message":message})
