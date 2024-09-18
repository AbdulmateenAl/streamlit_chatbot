import streamlit as st
import pandas as pd
from scraper import create_table

st.title("Here is my first streamlit app")

st.text_input("Your name", key="name")
url = st.session_state.name

if url:
    movies = create_table(url)

    df = pd.DataFrame(movies, columns=['title'])
    st.table(df)