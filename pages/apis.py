import streamlit as st 
import requests

st.title("Overview of our project")
st.write("Ali, Jared, Zuchi, Nile")

st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
)


if st.button("Fetch Overview"):
    st.write("This dataset gives a simulated look into how students are using AI tools like ChatGPT to support their academic work. With 10,000 sessions across different grade levels and subjects, it captures real-world-style interactions where students use AI for writing, coding, studying, brainstorming, and more. Each session includes details like the student's academic level, task type, session length, how effective the AI was, satisfaction ratings, and whether the student reused the tool. It's designed for exploratory data analysis, data visualization, and machine learning projects focused on understanding AI's growing role in education. ")

st.write(
    """
    ----------------------------------------------------------------------------------------------------
    """
)
st.write("Down is an example of how we used AI in our project, This graph is made entirely by chatGPT. Stimulating the usefulness that AI can have during school/work settings")
st.image("data/ai_usage_student_life_graph.png", width=700)
st.write("The graph shows how students use AI with different session lengths and numbers of prompts, with bubble size being their final outcome scores. Color shows the level of AI support, with shape representing the type of task completed. It reveals patterns between AI usage intensity, task type, and student performance.")