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
st.title("A Data Overview of AI Being Used in Student Life ")

st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
)

col1, col2 = st.columns(2)
with col1:
    st.image("/workspaces/Maybe-project/data/Uchibro.jpg", width=250)
with col2:
    st.image("/workspaces/Maybe-project/data/spongebob-study.gif", width=400)

st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
)

st.title("Data Table")
st.write("""Explore how students at different academic levels use AI tools like ChatGPT for tasks such as coding, writing, studying, and brainstorming.""")
         
data = pd.read_csv("/workspaces/Maybe-project/data/ai_assistant_usage_student_life.csv")

# ...existing code...

# ...existing code...

tab1, tab2, tab3, tab4 = st.tabs(["Data", "Task Type Pie", "Reuse Pie", "Prompts Bar"])

with tab1:
    st.write("This is your Data tab.")
    st.dataframe(data)

with tab2:
    st.write("Task Types Served by AI Assistant")
    task_counts = data['TaskType'].value_counts().reset_index()
    task_counts.columns = ['TaskType', 'count']
    chart = alt.Chart(task_counts).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field='count', type='quantitative'),
        color=alt.Color(field='TaskType', type='nominal'),
        tooltip=['TaskType', 'count']
    ).properties(title='Task Types Served by AI Assistant')
    st.altair_chart(chart, use_container_width=True)

with tab3:
    st.write("Did Students Reuse the AI Assistant?")
    usage_counts = data['UsedAgain'].value_counts().reset_index()
    usage_counts.columns = ['UsedAgain', 'Count']
    fig = px.pie(usage_counts, names='UsedAgain', values='Count', title='Did Students Reuse the AI Assistant?')
    st.plotly_chart(fig)

with tab4:
    st.write("Total AI Prompts by Academic Level")
    chart = alt.Chart(data).mark_bar().encode(
        x='StudentLevel:N', y='TotalPrompts:Q',
        tooltip=['StudentLevel', 'TotalPrompts']
    ).properties(title='Total AI Prompts by Academic Level')
    st.altair_chart(chart, use_container_width=True)
