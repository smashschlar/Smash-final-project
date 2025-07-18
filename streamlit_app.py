import altair as alt
import pandas as pd
import streamlit as st


pages = {
    "Project Pages":
    [
        st.Page("pages/apis.py", title = "Project Overview"),
        st.Page("pages/AIinstudents.py", title = "The AI student data page"),
        st.Page("pages/experimental.py", title = "experimental page"),
    ]
}

pg = st.navigation(pages)
pg.run()

