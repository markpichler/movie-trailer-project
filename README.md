# Mark's Favorite Flicks (AKA Movie Trailer Website)
This is my first project submission for Udacity's Full Stack Web Developer Nanodegree program.  It generates a webpage of a running list of my all-time favorite movies.  

To customize my project, I made some alterations to the Fresh Tomatoes code (provided by Udacity) mainly to include movie overview info as well as scattered CSS changes.  I also needed to adjust the code slightly in order to integrate the data given by the TMDb API (e.g. Fresh Tomatoes accepts a YouTube URL, but the API returns a YouTube video ID).

# Setup
This program makes use of two Python packages not included in the Python Standard Library; _tmdbsimple_ and _requests_.  To set up the environment, simply type the following in the terminal:
```
pip install -r requirements.txt
```

# Launching the Program
To launch the program, run the `entertainment_center.py` module.

# Powered By
* [Fresh Tomatoes](https://github.com/udacity/ud036_StarterCode) - Foundation code used to generate webpage 
* [The Movie Database (TMDb)](https://www.themoviedb.org/) - API used to pull movie info 
* [tmdbsimple](https://github.com/celiao/tmdbsimple) - TMDb API wrapper for Python
