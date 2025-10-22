import gradio as gr
from transformers import pipeline
import torch

# Load model
sentiment_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english",dtype=torch.float16)

# Define function for Gradio
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return f"Predicted label: {result['label']} (Score: {result['score']:.2f})"

# Create Gradio interface
demo = gr.Interface(fn=analyze_sentiment, inputs="text", outputs="text", title="Sentiment Analysis")

if __name__ == "__main__":
    demo.launch()