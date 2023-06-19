import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
        movie_id = i[0]
        # Fetch poster from API
        recommend_movies.append(movies["title"][i[0]])

    return recommend_movies


movies_dict = pickle.load(open('Top-1000-movies-recommender.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox("Enter the movie you have currently watched", movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write(f"Recommending top 5 movies similar to {selected_movie_name}...")
    for i in recommendations:
        st.write(i)

