import streamlit as st
import pickle
from PIL import Image
import os

import pandas as pd
import requests
from pathlib import Path


cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
prof_pic = cur_dir / "assets" / "photo.jpg"

# Description
PAGE_TITLE = "Movies Recommendation"
PAGE_ICON = "✨"
NAME = "VIVEK KUMAR"
DESCRIPTION = """
I am a CSE student, currently in 3rd year and enthusiastic in data science, data analysis & Machine Learning, aspire to learn new thing at every second. 
Fan of 07
"""
EMAIL = "viveksinghpihuli@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/vivekbholu/",
    "GitHub": "https://github.com/Bholuvivek",
}
PROJECTS_REQUIRMENTS_DONE= {
    "🍿🍿 The Things are done so far for this project......",
    "🏆 All the information are scraped from flipkart.com and are produced the raw data in a .csv file",
    "🏆 Cleaning and do all the preprocessing task through pandas library of python to get a clean dataframe",
    "🏆 Done the data preprocessing task by regex in python",
    "🏆 Done all the visualization task through plotly library of python"
    "🏆 Making the model through Random Forest Regressior, to get the desired prediction of laptop prize 😊"
    "🏆 Last but not the list make the website through streamlit framework through python and deploy in "
    "streamlit app."
}


def fetch_poster(movie_id):
   response = requests.get(
       'https://api.themoviedb.org/3/movie/{}?api_key=8f81c4157b9b645897a184be13524659&language=en-US'.format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similar[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
      movie_id = movies.iloc[i[0]].movie_id
      #fetching poster from api
      recommended_movies.append(movies.iloc[i[0]].title)
      recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similar = pickle.load(open('sam.pkl', 'rb'))

st.title("Movie Recommender System")
st.subheader(["This is Developed By Vivek Singh BHolu"])

st.subheader("welcome all, let's enjoy together😎😎😎😎")


prof = Image.open(prof_pic)


# Header section

col7, col8 = st.columns(2, gap = "small")
with col7:
    st.image(prof, width=220)

with col8:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📩", EMAIL)

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.subheader("Knowledge & Self-declaration ")
st.write(
    """
- ✔️ Currently a student, studied in 3rd year
- ✔️ Intermediate knowledge in python, still exploring and trying to grasp a good hand in python
- ✔️ Has understanding in data science and trying to find the hardness behind the easy word ML 
- ✔️ Has team management and problem solving capability
- ✔️ Always try to learn new things through challenges and tasks 
- ✔️ Some time get confused to himself and has somewhat little patience
"""
)
st.subheader("Project Name - Movies Recommendation")



selected_movie_name = st.selectbox(
    'Select the movie from the list below',
    movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
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
    