from flask import render_template
from app import app
from .request import get_movies

#views 
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The Best best Movie Review Website Online'
    # message = 'Hello World'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View root page function theat returns the index pages and its  data 
    '''
    return render_template('movie.html',  id = movie_id)