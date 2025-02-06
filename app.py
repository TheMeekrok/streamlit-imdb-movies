import streamlit as st

st.set_page_config(page_title="OVERVIEW | IMDB movie dataset", page_icon="🎥")

pg = st.navigation(
    [
        st.Page("./pages/overview.py", title="Overview", icon="🎥"),
        st.Page("./pages/analisys.py", title="Analisys", icon="🔍"),
    ]
)

pg.run()
