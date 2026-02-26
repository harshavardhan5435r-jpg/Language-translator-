import os
from google import genai
from dotenv import load_dotenv
import gradio as gr 

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def multi_language_translator(text, language):
    prompt = f"Translate the following text into {language}: {text}"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "temperature": 0.3,
            "max_output_tokens": 500,
        }
    )
    return response.text
# Gradio UI
demo = gr.Interface(
    fn=multi_language_translator,
    inputs=[
        gr.Textbox(label="Enter Text", placeholder="Type something...", lines=4),
        gr.Textbox(label="Enter Language", placeholder="e.g. Telugu, Hindi, French...")
    ],
    outputs=gr.Textbox(label="Translation", lines=4),
    title="🌍 Multi Language Translator",
    description="Type any text and any language — Gemini will translate it!"
)

demo.launch()

