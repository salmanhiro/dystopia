import streamlit as st
import os
import openai
import string
import tensorflow_hub as hub
import numpy as np
import tensorflow as tf
from PIL import Image


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

def generate_nightmare(input_image, style_image):
    content_image = np.asarray(content_image).astype(np.float32)[np.newaxis, ...] / 255.
    style_image = np.asarray(style_image).astype(np.float32)[np.newaxis, ...] / 255.
    # Optionally resize the images. It is recommended that the style image is about
    # 256 pixels (this size was used when training the style transfer network).
    # The content image can be any size.
    style_image = tf.image.resize(style_image, (256, 256))

    # Load image stylization module.
    hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0]
    return stylized_image

st.header("Future dystopian story")


# Use Streamlit to get the length of the random word from the user
year = st.slider("Choose the year (from 2022 to 3000):", min_value=2025, max_value=3000, value=2025)

# Generate random word
words = generate_story(year)

# Use Streamlit to display the random word
st.write("OpenAI prompted:", words)

files = st.drag_and_drop_files("Choose an image file")

if files:
    content_image = Image.open(files[0])
    style_image = Image.open('1950670.jpg')
    output_image = generate_nightmare(content_image, style_image)
    st.image(output_image, caption="Generated dystopian image", use_column_width=True)



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
        <p>Dystopia is a project to inform everyone that AI is not all about building the positive and bright future. 
        It's just the same storyteller when we asked about the pessimism.
        However this is a journey for me to know about the reason of how the AI could think like that. Training data?
        
        </p>
        <p>Created with GPT and Tensorflow</p>
    </div>
    """,
    unsafe_allow_html=True,
)