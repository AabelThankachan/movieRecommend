import streamlit as st
import pickle
import requests
import gzip

def fetch_poster(id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=801e2317bffca3ca97d07efa1adfe1af&language=en-US".format(id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:

        id=movies.iloc[i[0]].id

        recommended_movies.append(movies.iloc[i[0]].title)

        #fetch poster from API
        recommended_movies_posters.append(fetch_poster(id))

    return recommended_movies, recommended_movies_posters

import os
movies = pickle.load(open(os.path.join("code", "movies.pkl"), "rb")) #movies is a DataFrame
#movies = movies['title'].values

#similarity=pickle.load(open("similarity.pkl", "rb"))
with gzip.open(os.path.join("code", "similarity.pkl.gz"), "rb") as f:
    similarity = pickle.load(f)


st.title("Movie Recommendation System")

selected_movie=st.selectbox("Select movie", movies['title'].values)

if(st.button("Recommend")):
    names,posters=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])                
    