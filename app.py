import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title("Movie Recommender System")

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=55ff7adc3f7935d5e70d6b3f17fd62a0&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def top_5_recommend_movie(movie):
    # Show loading spinner while fetching recommendations
    with st.spinner('Loading List...'):
        current_movie_index = movies[movies['title'] == movie].index[0]
        current_movie_distance_with_others = similarity[current_movie_index]
        movies_list = sorted(list(enumerate(current_movie_distance_with_others)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movie_posters = []
        for movie in movies_list:
            movie_id = movies.iloc[movie[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movies.append(movies.iloc[movie[0]].title)
    return recommended_movies, recommended_movie_posters

selected_movie_name = st.selectbox(
    'Search Movie', movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movies,recommended_movie_posters = top_5_recommend_movie(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.html('<br />')
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.html('<br />')
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movies[2])
        st.html('<br />')
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.html('<br />')
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.html('<br />')
        st.image(recommended_movie_posters[4])






# if st.button('Recommend'):
#     recommendation = top_5_recommend_movie(selected_movie_name)
#     for movie_item in recommendation:
#         st.write(movie_item)