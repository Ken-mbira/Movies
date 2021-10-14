from django.shortcuts import render
from . import requests

def index(request):
    """This will render the home page

    Args:
        request ([type]): [description]
    """
    random_data = requests.discover_request('discover','popularity.desc')
    processed = requests.process_data(random_data)
    return render(request,'movie/index.html',{'movies':processed})

def movie_spec(request,id):
    """This will  return the movie instance and render its contents onto the image page

    Args:
        request ([type]): [description]
        id ([type]): [description]
    """
    movie = requests.movie_request(id)
    return render(request,'movie/movie.html',{'movie':movie})
