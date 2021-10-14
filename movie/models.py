from django.db import models

class Movie():
    """This defines the structure of a movie instance
    """
    def __init__(self,id,title,description,image_path):
        self.id = id
        self.title = title
        self.description = description
        self.image_path = image_path