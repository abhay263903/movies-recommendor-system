import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}/images?api_key=8265bd1679663a7ea12ac168da84d2e8'.format(movie_id))
    data = response.json()
    return data

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(similarity[0])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        # facthing poster

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

import os
import pickle
import gdown

FILE_ID = "13awgttkztE6fEYqZdw3wPbyTDYcdlMrL"
FILE_PATH = "similarity.pkl"

if not os.path.exists(FILE_PATH):
    gdown.download(
        id=FILE_ID,
        output=FILE_PATH,
        quiet=False
    )

with open(FILE_PATH, "rb") as file:
    similarity = pickle.load(file)

movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

Selected_Movie_Name = st.selectbox(
    "How would you like to be contacted?", movies['title'].values )

if st.button("RECOMMEND"):
    recommendations = recommend(Selected_Movie_Name)
    for i in recommendations:
        st.write(i)
