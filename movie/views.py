from django.shortcuts import render

def index(request):
    """This will render the home page

    Args:
        request ([type]): [description]
    """
    return render(request,'movie/index.html')
