#testing purposes 
import altair as alt
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import kagglehub
from kagglehub import KaggleDatasetAdapter
import numpy as np
import plotly.express as px

st.set_page_config(page_title="AI Assistant Usage in Student Life")
st.title("A Data Overview of AI Being Used in Job Trends")

st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
)

col1, col2 = st.columns(2)
with col1:
    st.image("/workspaces/Smash-final-project/data/kids-in-professional-uniform-children-doing-different-job-as-builder-teacher-businessman-doctor-and-firefighter-vector.jpg", width=250)

st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
)

st.title("Data Table")
st.write("""This dataset explores how Artificial Intelligence (AI) is transforming the global job market. With a focus on identifying which jobs are increasing or decreasing due to AI adoption, this dataset provides insights into job trends, automation risks, education requirements, gender diversity, and other workforce-related factors across industries and countries.""")
         
data = pd.read_csv("/workspaces/Smash-final-project/data/ai_job_trends_dataset.csv")


tab1, tab2, tab3, tab4 = st.tabs(["Data", "Bar Chart", "Reuse Pie", "Prompts Bar"])

with tab1:
    st.write("This is your Data tab.")
    st.dataframe(data)

with tab1:
    st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
    )
    st.write("The AI Job Trends data provides a clear snapshot of the evolving job market for artificial intelligence. One job posting is listed per row, with chosen information consisting of the job name, company, location, and entire text job description. It covers skills needed—from rudimentary programming languages like Python to more specialized AI tools like TensorFlow and natural language processing (NLP) libraries—giving insight into the technicalities of occupations. Data also includes employment categories (e.g., full-time, contract) and salary estimates where available, allowing examination by location and occupation of compensation patterns. Including URLs on job postings provides immediate access to actual postings, and the date column allows tracking of demand by time. These twin functionalities make the dataset worthwhile to researchers, job seekers, and workforce analysts wanting to know how the AI job market is changing in terms of skill requirements, geographic demand, and industry take-up.")


with tab2:
 # Title
    st.title("AI Job Trends Dashboard")
    df = pd.read_csv("/workspaces/Smash-final-project/data/ai_job_trends_dataset.csv")  
    st.subheader("Preview of Dataset")
    st.dataframe(df.head())
    st.subheader("Projected Job Openings in 2030 by AI Impact Level")
    impact_data = df.groupby("AI Impact Level")["Projected Openings (2030)"].sum().reset_index()
    bar_chart = alt.Chart(impact_data).mark_bar().encode(
    x=alt.X('Projected Openings (2030):Q', title='Projected Openings (2030)'),
    y=alt.Y('AI Impact Level:N', sort='-x'),
    color='AI Impact Level:N',
    tooltip=['AI Impact Level', 'Projected Openings (2030)']
    ).properties(width=600)
    st.altair_chart(bar_chart)
