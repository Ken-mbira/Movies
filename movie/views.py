from django.shortcuts import render
from . import requests

def index(request):
    """This will render the home page

    Args:
        request ([type]): [description]
    """
    random_data = requests.request('discover','popularity.desc')
    processed = requests.process_data(random_data)
    return render(request,'movie/index.html',{'movies':processed})
