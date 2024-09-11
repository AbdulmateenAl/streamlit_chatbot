import streamlit as st
import pandas as pd

st.title("Here is my first streamlit app")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))