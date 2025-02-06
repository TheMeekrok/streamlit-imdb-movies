import streamlit as st
import pandas as pd
import numpy as np


def create_sidebar_filters(data: pd.DataFrame):
    st.sidebar.title("Filters")

    # Add year column to be able to sort by year
    data["year"] = pd.to_datetime(data["release_date"], format="mixed").dt.year

    vote_average = st.sidebar.slider("vote_average", 0, 10, (0, 10))

    unique_genres = list(
        set(
            genre.strip()
            for row in data["genres"].fillna("").unique()
            if row
            for genre in row.split(",")
        )
    )

    unique_genres.insert(0, "All")
    genre = st.sidebar.selectbox("genre", unique_genres)

    unique_original_languages = data["original_language"].unique()
    unique_original_languages = np.insert(unique_original_languages, 0, "All")
    original_language = st.sidebar.selectbox(
        "original_language", unique_original_languages
    )

    min_year = int(data["year"].min())
    max_year = int(data["year"].max())
    year = st.sidebar.slider("year", min_year, max_year, (min_year, max_year))

    budget_max = int(data["budget"].max())
    budget = st.sidebar.slider("Budget range", 0, budget_max, (0, budget_max))

    return vote_average, genre, original_language, year, budget


def create_sidebar(data: pd.DataFrame):
    filters = create_sidebar_filters(data)

    return filters
