# Aniemore

Aniemore is a Python library for working with text recognition and emotion recognition models. This repository contains a Streamlit app that demonstrates how to use the Aniemore library for emotion recognition.

Main screen 

<img width="545" alt="image" src="https://user-images.githubusercontent.com/44744458/236799468-0f638d50-0415-41c4-a140-819baf062380.png">

This web application containing 2 docker containers with DB (Redis) + Web (Streamlit) architecture.

## Prerequisites
Before running the app, you must have the following installed:

- Python 3.7 or later
- Docker
- Docker Compose

### Prepare directory

- Clone repo
- Move to the aniemore_st folder

Structure should be:

<img width="289" alt="image" src="https://user-images.githubusercontent.com/44744458/236801244-269670fd-288a-44c2-b0f3-344a27d84c73.png">

## Docker Compose

If you prefer to run the app in a Docker container, you can use Docker Compose to build and run the container:

1. Build the Docker image:

   ```
   $ docker-compose build
   ```

2. Start the Docker container:

   ```
   $ docker-compose up
   ```

   The app should now be running at `http://localhost:8501`.

## License

Aniemore is released under the [MIT License](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/blob/main/LICENSE).
