FROM python:3.9

# Install Streamlit and other dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Add the app files to the image
ADD . /src

# Set the working directory to the app directory
WORKDIR /src

EXPOSE 8501

# Run the app
CMD streamlit run src/app.py