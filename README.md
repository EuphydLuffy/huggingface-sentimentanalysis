---
title: Deployment of a Gradio application with Docker to Hugging Face Spaces
emoji: "🤖"
colorFrom: "blue"
colorTo: "green"
sdk: "docker"
sdk_version: "1.0"
app_file: "Dockerfile"
pinned: false
---
## Try the App

Check out the live Gradio app on Hugging Face Spaces:  
[![Open on Hugging Face](https://img.shields.io/badge/Open%20on-Hugging%20Face-blue)](https://huggingface.co/spaces/EuphyTheLuffy/SentimentAnalysisGradioApp)

## Project Overview

This project demonstrates how to deploy a Gradio application in a fully automated CI/CD workflow using Docker and Hugging Face Spaces. This APP leverages a DistilBERT model fine-tuned for sentiment analysis and builds an interactive Gradio interface that users can access directly from the web.

Key highlights:

- End-to-end development workflow: Code, test, and run locally.

- Automatic CI/CD-enabled deployment with GitHub Actions: Deploys the app to Hugging Face Spaces whenever a commit is pushed to the main branch, following a streamlined workflow.

- Dockerized environment: Ensures consistent dependencies and environment both locally and on Hugging Face.

- Interactive deployment: Hugging Face automatically builds and runs the container, giving you a live Gradio app accessible online.

## Installation
Install all dependencies using pip install -r requirements.txt (or "make install") after cloning the repo.

## Usage
1. Clone the repository to your local machine.
2. Install the packages listed in requirements.txt (or run "make install" in bash).
3. Makefile commands:
   - Check code style:
      ```
      make lint
      ```
   - Format code:
      ```
      make format
      ```
   - Run tests through pytest:
      ```
      make test
      ```  
   - Launch the Gradio app locally:
      ```
      make launch
      ```

4. Test the container locally:
   - Build the Docker image:
     ```
     docker build -t sentiment-app .
     ```
   - Run the Docker container:
     ```
     docker run -p 7860:7860 sentiment-app
     ```

5. Deploy to Hugging Face Spaces through Github Action worflow:
   - Go to Github UI, under actions and run the "Build and Deploy to Hugging Face Spaces" workflow.

## Repository Structure
- `app.py`: The main Gradio application file.
- `test_app.py`: Unit tests for the DistiltBert sentiment analysis model.
- `Dockerfile`: Docker configuration file for building the application container.
- `requirements.txt`: List of Python dependencies required for the application.
- `Makefile`: Contains commands for linting, formatting, testing, and launching the app.
- `.github/workflows/main.yml`: defines CI deployment workflow. 
