import altair as alt
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import kagglehub
from kagglehub import KaggleDatasetAdapter
import numpy as np
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("data/ai_assistant_usage_student_life.csv")
    return df

df = load_data()
chart = alt.Chart(df).mark_bar().encode(
    x='StudentLevel:N', y='TotalPrompts:Q',
    tooltip=['StudentLevel', 'TotalPrompts']
).properties(title='Total AI Prompts by Academic Level')
st.altair_chart(chart, use_container_width=True)