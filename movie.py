# Purpose:
# Stores movie data including title, image url and trailer url
# Usage:
# the constructor requires the title of the movie, a url of poster image
# and a youtube url for the trailer
# Available methods:
# Parameterized Constructor
class Movie():
    def __init__(self, movie_title, movie_poster_image_url, movie_youtube_url):
    	self.title = movie_title
    	self.poster_image_url = movie_poster_image_url
    	self.trailer_youtube_url = movie_youtube_url
