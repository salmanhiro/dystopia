import streamlit as st
import os
import openai
import string
import numpy as np
import random

os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

st.markdown("""
  <style>
    pre {
      font-family: "Consolas", monospace;
      font-size: 14px;
    }
  </style>
""", unsafe_allow_html=True)

# Use the st.code function to display a console message
st.title("DYSTOPIA")

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

st.header("Selected interesting music video to accompany your dystopian journey")
st.code("Yes i just want to introduce the artists because i love them")

# Get the URL of the YouTube video
video_url = "https://www.youtube.com/watch?v=xPDphbUyFJ4"

# Use the st.audio function to play the YouTube video
st.video(video_url)

def generate_story(year):
    context = 'disaster'
    population = 'human'
    country = 'worldwide'
    # Define the prompt for the story
    prompt = f"Generate a story about {context} in {year} to world in which human become severely endangered"

    # Use the GPT-3 model to generate the text for the story
    model_engine = "text-davinci-002"
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1048, temperature=0.7)
    story = completion["choices"][0]["text"].strip('\n')
    return story

st.header("Future dystopian story")


# Use Streamlit to get the length of the random word from the user
year = st.slider("Choose the year (from 2022 to 3000):", min_value=2025, max_value=3000, value=2025, step=5)

# Generate random word
words = generate_story(year)

# Use Streamlit to display the random word
st.write("OpenAI prompted:", words)

# Add a footer
st.markdown(
    """
    <style>
        .footer {
            text-align: center;
        }
    </style>
    <div class='footer'>
        <hr>
        <p>
        Dystopia is a project to inform everyone that AI is not all about building the positive and bright future. 
        It's just the same storyteller when we asked about the pessimism.
        However this is a journey for me to know about the reason of how the AI could think like that. Training data?
        
        By <a href="https://salmanhiro.vercel.app/">salmanhiro</a>
        Created with GPT and Tensorflow
    </div>
    """,
    unsafe_allow_html=True,
)