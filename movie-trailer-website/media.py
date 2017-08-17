class Movie():
    """Defines the basic properties of a movie.
    Attributes:
        title (str): Movie title.
        overview (str): Description of movie.
        poster (str): URL to movie poster.
        trailer (str): YouTube URL to movie trailer.
    """
    def __init__(self, title, overview, poster, trailer):
        self.title = title
        self.overview = overview
        self.poster_img_url = ("http://image.tmdb.org/t/p/original"
                               str(poster))
        self.trailer_youtube_url = trailer
