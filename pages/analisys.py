import streamlit as st

from components.charts import (
    bar_month_vs_revenue,
    most_popular_film,
    original_language_distribution,
    scatter_budget_vs_popularity,
    scatter_budget_vs_revenue,
    scatter_runtime_vs_budget,
    vote_average_distribution,
)
from components.sidebar import create_sidebar
from utils.data_filter import filter_data
from utils.data_loader import load_data

st.title("Analisys")

data = load_data()
filters = create_sidebar(data)

data = filter_data(data, filters)

st.markdown("## Simple metrics")
most_popular_film(data)
vote_average_distribution(data)
scatter_budget_vs_revenue(data)
scatter_runtime_vs_budget(data)
original_language_distribution(data)

st.markdown("## Advanced metrics")
bar_month_vs_revenue(data)
scatter_budget_vs_popularity(data)
