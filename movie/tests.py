from django.test import TestCase

from .models import Movie

class TestMovie(TestCase):
    """This will test a movie instance

    Args:
        TestCase ([type]): [description]
    """
    def setUp(self):
        """
        This will run before the tests do
        """
        self.movie = Movie(1,'Movie',"This is the best movie to be created","link to image","link to trailer")

    def test_movie_instance(self):
        """This tests whether a movie instance is of the class Movie
        """
        self.assertTrue(isinstance(self.movie,Movie))