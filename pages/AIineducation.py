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
    st.image("/workspaces/Smash-final-project/data/Uchibro.jpg", width=250)
with col2:
    st.image("/workspaces/Smash-final-project/data/spongebob-study.gif", width=400)

st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
)

st.title("Data Table")
st.write("""Explore how students at different academic levels use AI tools like ChatGPT for tasks such as coding, writing, studying, and brainstorming.""")
         
data = pd.read_csv("/workspaces/Smash-final-project/data/ai_assistant_usage_student_life.csv")


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
with tab4:
    st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
    )
    st.write('The bar graph titled **"Total AI Prompts by Academic Level"** shows the number of AI prompts submitted by students at the graduate, high school, and undergraduate levels. Undergraduate students submitted the highest number of prompts, with totals nearing 34,000, while both graduate and high school students submitted significantly fewer, at around 12,000 each. This suggests that undergraduate students are the most active users of AI tools among the three academic levels.')

with tab3:
    st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
    )
    st.write('The pie chart titled **"Did Students Reuse the AI Assistant?"** illustrates the percentage of students who chose to reuse the AI assistant versus those who did not. A significant majority, **70.6%**, indicated that they reused the AI assistant, suggesting a strong level of satisfaction, usefulness, or reliance on the tool for academic support. In contrast, **29.4%** of students did not return to use the assistant again. This data highlights the overall positive reception of AI assistance among students and may reflect its perceived effectiveness in helping them complete tasks, solve problems, or enhance their learning experience. The high reuse rate implies that AI tools are becoming an integral part of the student learning process.')

with tab2:
    st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
    )
    st.write('The donut chart titled **"Task Types Served by AI Assistant"** illustrates the different types of academic tasks for which students utilized an AI assistant. The chart includes six categories: Brainstorming, Coding, Homework Help, Research, Studying, and Writing. Among these, **Writing** and **Studying** occupy the largest portions of the chart, indicating that students most frequently relied on AI for help with composing written content and preparing for exams or understanding material. **Homework Help** and **Coding** also represent significant segments, suggesting a strong demand for support in problem-solving and programming tasks. In contrast, **Brainstorming** and **Research** are the smallest segments, implying they were the least common uses of the AI assistant. Overall, the chart shows that students leveraged the AI assistant most heavily for content generation and academic preparation.')

with tab1:
    st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
    )
    st.write('This dataset contains detailed records of 10,000 AI assistant usage sessions by students across various academic disciplines and levels. Each entry includes information such as the session date, student level (e.g., undergraduate), academic discipline (e.g., Computer Science, Psychology), session length in minutes, number of prompts used, type of task (e.g., Studying, Coding, Writing), and the AI assistance level provided. It also records the final outcome of the session (e.g., assignment completion), whether the student chose to use the assistant again, and their satisfaction rating. This structured data enables analysis of AI usage patterns, effectiveness, and user satisfaction in the context of student life and academic support.')
