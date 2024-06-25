import pandas as pd

def load_data():
    ratings = pd.read_csv('data/ml-latest-small/ratings.csv')
    movies = pd.read_csv('data/ml-latest-small/movies.csv', usecols=['movieId', 'title'])
    
    return ratings, movies

def preprocess_data(ratings, movies):
    combined = pd.merge(ratings, movies, on='movieId')
    user_movie_matrix = combined.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    
    return user_movie_matrix
    # return combined