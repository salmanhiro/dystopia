# Dystopia
AI to generate dystopian scenery and narrative

## GPT-3 Dystopian Scenery

This prompt will generate disaster in certain time from GPT-3. Don't know the reason behind, is the result random or science-backed? As we know that the machine learning learns from training dataset. 

## Nightmare Scenery

This prompt use Google magenta model to simulate image styling to a chaotic scenery. This is more explainable as there's no big underlying question. 

## References

Both of part were made from the discussion with ChatGPT about the future of humanity, will it be utopian or dystopian. Unfortunately, given current climate and international actions, dystopian ending seems like the canonical one. Technically made with Tensorflow and OpenAI.

## OpenAI API Key

This project needs OpenAI API key, which can be acquired at `https://beta.openai.com/account/api-keys`. Just log in to OpenAI beta trial and look at the account menu.

## How to use
```
1. Install docker. If you don't familiar with it, familiarize first with docker tutorial.
2. Build with docker, docker build -t dystopia .
3. Run with docker, docker run -e OPENAI_API_KEY dystopia
4. The default streamlit container is 8501, however, you can specify it in docker build by bind the host and container's port. In example -p 8501:8000
```