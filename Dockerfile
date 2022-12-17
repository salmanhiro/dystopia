FROM python:3.9

# Install Streamlit and other dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN pip install protobuf~=4.21.1
# Add the app files to the image
ADD . /src

# Set the working directory to the app directory
WORKDIR /src

# Run the app
CMD streamlit run src/app.py