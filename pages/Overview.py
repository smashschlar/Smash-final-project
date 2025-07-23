import streamlit as st 
import requests as req
import pandas as pd
import altair as alt

st.title("Overview of our project")
st.write("Ali, Jared, Zuchi, Nile")

st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
)


if st.button("Fetch Overview"):
    st.write("Our project explores how artificial intelligence (AI) is being integrated into key areas of modern life, with a focus on sectors such as employment and education. By analyzing a collection of diverse datasets, we aim to uncover patterns in the adoption and impact of AI technologies. In the job market, we examine trends in AI-related roles, required skills, and industry demand, highlighting how companies are reshaping their workforce to include AI expertise. In education, we investigate how AI is transforming learning environments, from personalized tutoring systems to curriculum enhancements that prepare students for an AI-driven future. Through this data-driven approach, our project offers a comprehensive view of how AI is not only influencing the way people work and learn, but also reshaping societal expectations and institutional structures.")

st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
)
st.write("Down is an example of how we used AI in our project, This graph is made entirely by chatGPT. Stimulating the usefulness that AI can have during school/work settings")
st.image("data/ai_usage_student_life_graph.png", width=700)
st.write("The graph shows how students use AI with different session lengths and numbers of prompts, with bubble size being their final outcome scores. Color shows the level of AI support, with shape representing the type of task completed. It reveals patterns between AI usage intensity, task type, and student performance.")

#hello nicole for testing purposes
