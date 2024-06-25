import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarty(user_movie_matrix):
    # Computing the cosine similarity matrix
    similarity_matrix = cosine_similarity(user_movie_matrix)
   
    return similarity_matrix

def recommend_movies(user_id, user_movie_matrix, movies, n_recommendations=5):
    # Calculating similarity matrix
    similarity_matrix = calculate_similarty(user_movie_matrix)
    # Getting the similarity scores for the given user_id
    user_similarity_score = similarity_matrix[user_id - 1] # user_id - 1 because indices start from 0
    # Sorting the scores in descending order and get the indices of the most similar users
    similar_users_indices = user_similarity_score.argsort()[::-1]
    
    # Recommend movies from the top similar users
    recommended_movies = {}
    for similar_user in similar_users_indices:
        if similar_user == user_id - 1:
            continue  # Skip the same user
        similar_user_ratings = user_movie_matrix.iloc[similar_user]
        for movie_id in similar_user_ratings.index:
            if user_movie_matrix.iloc[user_id - 1][movie_id] == 0:  # Recommend only movies not yet rated by the user
                if movie_id not in recommended_movies:
                    recommended_movies[movie_id] = similar_user_ratings[movie_id]
                else:
                    recommended_movies[movie_id] += similar_user_ratings[movie_id]
        if len(recommended_movies) >= n_recommendations:
            break
    
    # Sort the recommended movies by score
    recommended_movies = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)
    # Get the movie titles
    recommended_movie_titles = [movies[movies['movieId'] == movie_id]['title'].values[0] for movie_id, _ in recommended_movies[:n_recommendations]]
    
    return recommended_movie_titles