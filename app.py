import streamlit as st
import pickle
import pandas as pd
import requests


# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/{}/movie/652?api_key=dc51451ceb1efbe48bac9bf6a0d0caa5&language=en-US'.format(movie_id))

#     data = response.json()
#     print(data)

#     return  "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]
    
    recommended_movie = []

    # recommended_movie_poster = []


    
    for i in movies_list:
        movie_id = i[0]
        # fetch poster from API 
        recommended_movie.append(movies.iloc[i[0]].title)
    
        # recommended_movie_poster.append(fetch_poster(movie_id))

    # return recommended_movie,recommended_movie_poster

    return recommended_movie


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


movies = pd.DataFrame(movies_dict)

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'How would like to be contacted',
    movies["title"].values
)

if st.button ('Recommend'):
    recommendation = recommend(selected_movie_name)

    # col1, col2, col3 = st.beta_columns(3)
        
    # with col1:
    #     st.header("A cat")
    #     st.image("https://static.streamlit.io/examples/cat.jpg")

    # with col2:
    #     st.header("A cat")
    #     st.image("https://static.streamlit.io/examples/cat.jpg")
    
    # with col3:
    #     st.header("A cat")
    #     st.image("https://static.streamlit.io/examples/cat.jpg")


    for i in recommendation:
        st.write(i)