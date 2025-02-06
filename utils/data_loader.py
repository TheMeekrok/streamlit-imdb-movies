import kagglehub
import os
import pandas as pd
import streamlit as st


@st.cache_resource
def load_data():
    path = kagglehub.dataset_download("anandshaw2001/imdb-data")
    file_name = "Imdb Movie Dataset.csv"
    file_path = os.path.join(path, file_name)

    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        return data

    else:
        return None
