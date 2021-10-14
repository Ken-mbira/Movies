from decouple import config
import urllib
import json

from .models import Movie

discover_url = "https://api.themoviedb.org/3/{}/movie?api_key={}&language=en-US&sort_by={}"
find_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'

API_KEY = config('API_KEY')

def discover_request(action,sort_by):
    """This function runs the request and retrieves the data

    Args:
        action ([type]): [description]
        sort_by ([type]): [description]

    Returns:
        [type]: [description]
    """
    url_path = discover_url.format(action,API_KEY,sort_by)
    serialized_data = urllib.request.urlopen(url_path).read()
    response = json.loads(serialized_data)
    return response

def process_data(random_data):
    """This will process the incoming data into a form more understood

    Args:
        data ([type]): [description]
    """
    arrays = random_data['results']
    returns = []
    for movie in arrays:
        id = movie['id']
        title = movie['original_title']
        description = movie['overview']
        path = movie['poster_path']
        image_path = f'https://image.tmdb.org/t/p/original/{path}'
        if path is not None:
            movie = Movie(id,title,description,image_path)
            returns.append(movie)

    return returns

def movie_request(id):
    """This will retur the details of a specific movie
    """
    url_path = find_url.format(id,API_KEY)
    serialized_data = urllib.request.urlopen(url_path).read()
    response = json.loads(serialized_data)

    id = id
    title = response['original_title']  
