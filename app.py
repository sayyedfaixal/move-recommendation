# import streamlit as st
# import pickle
# import pandas as pd
# import requests

# movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)

# similarity = pickle.load(open('similarity.pkl', 'rb'))


# st.title("Movie Recommender System")

# # """
# # def fetch_poster(movie_id):
# #     url = 'https://api.themoviedb.org/3/movie/{}?api_key=55ff7adc3f7935d5e70d6b3f17fd62a0&language=en-US'.format(movie_id)
# #     data = requests.get(url)
# #     data = data.json()
# #     poster_path = data['poster_path']
# #     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
# #     return full_path
# # '''
# # """


# def top_5_recommend_movie(movie):
#     # Show loading spinner while fetching recommendations
#     with st.spinner('Loading List...'):
#         current_movie_index = movies[movies['title'] == movie].index[0]
#         current_movie_distance_with_others = similarity[current_movie_index]
#         movies_list = sorted(list(enumerate(current_movie_distance_with_others)), reverse=True, key=lambda x: x[1])[1:6]

#         recommended_movies = []
#         recommended_movie_posters = []
#         for movie in movies_list:
#             movie_id = movies.iloc[movie[0]].movie_id
#             # recommended_movie_posters.append(fetch_poster(movie_id))
#             recommended_movies.append(movies.iloc[movie[0]].title)
#     return recommended_movies, recommended_movie_posters

# selected_movie_name = st.selectbox(
#     'Search Movie', movies['title'].values
# )

# if st.button('Show Recommendation'):
#     recommended_movies,recommended_movie_posters = top_5_recommend_movie(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movies[0])
#         st.html('<br />')
#         # st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movies[1])
#         st.html('<br />')
#         # st.image(recommended_movie_posters[1])

#     with col3:
#         st.text(recommended_movies[2])
#         st.html('<br />')
#         # st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movies[3])
#         st.html('<br />')
#         # st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movies[4])
#         st.html('<br />')
#         # st.image(recommended_movie_posters[4])




# if st.button('Recommend'):
#     recommendation = top_5_recommend_movie(selected_movie_name)
#     for movie_item in recommendation:
#         st.write(movie_item)
import streamlit as st
import pickle
import pandas as pd

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# App Title
st.title("🎥 Movie Recommender System")

st.markdown("""
    <style>
    .header {
        font-size: 24px;
        color: #2c3e50;
        font-weight: bold;
    }
    .movie-item {
        font-size: 18px;
        color: #ffffff;
        background-color: #34495e;
        padding: 10px;
        border-radius: 8px;
        margin: 5px 0;
        transition: transform 0.3s, background-color 0.3s;
        cursor: pointer;
    }
    .movie-item:hover {
        background-color: #1abc9c;
        transform: scale(1.05);
    }
    .footer {
        font-size: 14px;
        color: #7f8c8d;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="header">Welcome to the Movie Recommender System! 🌟</p>', unsafe_allow_html=True)
st.markdown('Select a movie from the dropdown, and get recommendations for similar movies.')

# Function to get top 5 recommended movies
def top_5_recommend_movie(movie):
    current_movie_index = movies[movies['title'] == movie].index[0]
    current_movie_distance_with_others = similarity[current_movie_index]
    movies_list = sorted(
        list(enumerate(current_movie_distance_with_others)),
        reverse=True, 
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = [movies.iloc[movie[0]].title for movie in movies_list]
    return recommended_movies

# User input for movie selection
selected_movie_name = st.selectbox(
    '🎬 Search for a movie:', 
    movies['title'].values
)

# Show recommendations on button click
if st.button('Show Recommendation'):
    recommended_movies = top_5_recommend_movie(selected_movie_name)

    st.markdown('<p class="header">Recommended Movies</p>', unsafe_allow_html=True)
    for idx, movie in enumerate(recommended_movies, start=1):
        st.markdown(
            f'<div class="movie-item">{idx}. {movie} 🎞️</div>', 
            unsafe_allow_html=True
        )

    st.markdown("""
        💡 *Unfortunately, movie posters are not available due to API restrictions.* 
        However, enjoy your personalized recommendations!
    """)

# Add footer
st.markdown('<p class="footer">🛠️ Built with Streamlit | ❤️ Happy Watching!</p>', unsafe_allow_html=True)
