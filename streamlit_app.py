import altair as alt
import pandas as pd
import streamlit as st


pages = {
    "Project Pages":
    [
        st.Page("pages/apis.py", title = "Project Overview"),
        st.Page("pages/AIinstudents.py", title = "The AI student data page"),
        st.Page("pages/experimental.py", title = "experimental page"),
        st.Page("pages/JANZBOT.py", title = "JANZBOT"),
    ]
}

pg = st.navigation(pages)
pg.run()

st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #000010 !important;
        color: #eaeaea !important;
        font-family: 'Courier New', monospace;
        font-size: 18px;
    }

    header, footer, .stDeployButton {visibility: hidden;}

    /* Remove padding/margins for full-screen look */
    .main {
        padding: 0rem 2rem;
    }

    h1, h2, h3, h4 {
        color: #1fb7ff;
        text-shadow: 0 0 5px #1fb7ff, 0 0 20px #1fb7ff;
    }

    .stButton > button {
        background-color: #1fb7ff;
        color: #000010;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 0.75em 1.5em;
        font-size: 1.1em;
        box-shadow: 0 0 15px #1fb7ff;
        transition: all 0.3s ease-in-out;
    }

    .stButton > button:hover {
        background-color: #00ffff;
        color: #000010;
        box-shadow: 0 0 25px #00ffff;
    }

    .neon-text-green { color: #00ffcc; text-shadow: 0 0 10px #00ffcc; font-weight: bold; }
    .neon-text-yellow { color: #fcee09; text-shadow: 0 0 10px #fcee09; font-weight: bold; }
    .neon-text-red { color: #ff073a; text-shadow: 0 0 10px #ff073a; font-weight: bold; }

    /* Optional: glowing div for feature highlight */
    .glow-banner {
        margin-top: 2rem;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        color: #1fb7ff;
        text-shadow: 0 0 10px #1fb7ff, 0 0 30px #00ffcc;
        animation: flicker 3s infinite;
    }

    @keyframes flicker {
        0% {opacity: 1;}
        50% {opacity: 0.85;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.contect.stip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break 

        response = chat_with_gpt(user_input)
        print("Chatbot", response)