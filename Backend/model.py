import pickle
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
import random
import os
import ast

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Clean up missing columns
movies = movies.dropna(axis=1)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Root route to avoid 404 on GET /
@app.route('/')
def index():
    return jsonify({"message": "Movie Recommender API is running."})

# Function to recommend movies
def recommend(movie_name):
    try:
        index = movies[movies['title'] == movie_name].index[0]
    except IndexError:
        return None
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [movies.iloc[i[0]].to_dict() for i in distances[1:31]]
    return recommended_movies

# Route to return 30 recommended movies
@app.route('/recommend/<name>', methods=['GET'])
def cosine_similarity(name):
    suggestions = recommend(name)
    if suggestions is None:
        return jsonify({"error": f"No movie found with name '{name}'"}), 404
    return jsonify(suggestions)

# Route to fetch unique genres
@app.route('/genres', methods=['GET'])
def get_unique_genres():
    genres_column = movies["genres"].dropna()
    all_genres = []

    for genre in genres_column:
        try:
            genre_list = ast.literal_eval(genre)
            all_genres.extend(genre_list)
        except (ValueError, SyntaxError):
            continue

    unique_genres = list(set(all_genres))
    capitalized_genres = [genre.capitalize() for genre in unique_genres]
    return jsonify(capitalized_genres)

# Route to fetch 30 random movies
@app.route('/movies/genres/all', methods=['GET'])
def get_random_movies_unfiltered():
    try:
        random_movies = movies.sample(n=30, random_state=random.randint(0, 999999999))
        return jsonify(random_movies.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

# Route to fetch 30 movies by genre
@app.route('/movies/genres/<genre>', methods=['GET'])
def get_movies_by_genre(genre):
    try:
        genre = genre.lower()

        def genre_match(gstr):
            try:
                genre_list = ast.literal_eval(gstr.lower())
                return genre in genre_list
            except (ValueError, SyntaxError):
                return False

        matching_movies = movies[
            movies['genres'].apply(lambda x: genre_match(x) if isinstance(x, str) else False)
        ]

        if matching_movies.empty:
            return jsonify({"message": f"No movies found for genre: {genre}"}), 404

        sampled_movies = matching_movies.sample(
            n=min(30, len(matching_movies)),
            random_state=random.randint(0, 999999999)
        )

        return jsonify(sampled_movies.to_dict(orient='records'))

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to fetch all movie titles
@app.route('/movies/titles', methods=['GET'])
def get_movie_titles():
    try:
        movie_titles = movies['title'].dropna().tolist()
        return jsonify(movie_titles)
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
