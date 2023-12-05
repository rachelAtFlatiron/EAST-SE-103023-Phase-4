#!/usr/bin/env python3

from flask import Flask

movies = [
    {
        "id": 1,
        "title": "Nope"
    },
    {
        "id": 2,
        "title": "Us"
    },
    {
        "id": 3,
        "title": "Titanic"
    }
]

app = Flask(__name__)

@app.route('/welcome_page')
def index():
    theater = 'Regal Cinemas'
    return f'<h1>Welcome to {theater}!</h1>'

@app.route('/sum/<int:num1>/<int:num2>')
def sum_of_two_numbers(num1, num2):
    print(f'num1 is a {type(num1)}')
    print(f'num2 is a {type(num2)}')
    return f'<h1>{num1 + num2}</h1>'
    # return {"sum": num1 + num2}

@app.route('/movies')
def get_movies():
    return movies

@app.route('/movies/<int:id>')
def get_one_movie(id):
    for movie in movies:
        if id == movie['id']:
            return movie
        
    return {"error": "Movie Not Found!"}

@app.route('/display_movies_website')
def display_movies():
    movie_list = ""

    for movie in movies:
        movie_list += f"<li>Movie # {movie['id']}: {movie['name']}</li>"

    return f"<ul>{movie_list}</ul>"

if __name__ == "__main__":
    app.run(port=7777, debug=True)