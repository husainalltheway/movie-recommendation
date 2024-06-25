from flask import Flask, render_template, request
from src.recommendation import recommend_movies
from src.data_preprocessing import load_data, preprocess_data
import os

app = Flask(__name__)

# Determine the absolute path to the templates directory
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src', 'templates'))
app.template_folder = template_dir

# Load and preprocess data
ratings, movies = load_data()
user_movie_matrix = preprocess_data(ratings, movies)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form['user_id'])
    recommendations = recommend_movies(user_id, user_movie_matrix, movies)
    return render_template('index.html', recommendations=recommendations, user_id=user_id)

if __name__ == '__main__':
    app.run(debug=True)
