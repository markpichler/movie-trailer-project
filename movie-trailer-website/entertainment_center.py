import fresh_tomatoes as ft
from media import Movie
import tmdbsimple as tmdb

# My API key required to access the TMDb API
tmdb.API_KEY = "26076ff2e7ca1e76051067205bfb682e"

# TMDb movie id's of my favorite movies; in no special order
id_array = [263115, 14254, 65086,  647, 138843, 82507, 177572, 293660, 1366,
            20352, 250546, 111, 254, 264660]

movie_array = []
# Iterate over id_array and pull appropriate data from TMDb then create and
# append Movie objects to movie_array.
for x in id_array:
    temp = tmdb.Movies(x)
    temp.info()  # Pull basic info for movie from TMDb
    temp.videos()  # Pull additional movie info from TMDb
    # Construct array of Movie objects
    movie_array.append(Movie(temp.title, temp.overview, temp.poster_path,
                             temp.results[0]["key"]))

# Call open_movies_page() after sorting movie_array by each Movie object's
# title attribute.
ft.open_movies_page(sorted(movie_array, key=lambda movie: movie.title))
