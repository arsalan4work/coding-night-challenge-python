import os # for evironment variables
import chainlit as cl # for chatbot interface
import google.generativeai as genai # for google genai api
from dotenv import load_dotenv # for loading enironment variables

load_dotenv() # Load environment variables from .env file

# Get Gemini API key from environment variables
gemini_api_key = os.getenv("GENAI_API_KEY")

genai.configure(api_key=gemini_api_key)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# chainlit decorator for when a new chat session starts
@cl.on_chat_start
async def handle_chat_start():
    # Send welcome message to user
    await cl.Message(content="Hello, Welcome to Arsalan's Chatbot. How can I help you today?").send()

# chainlit decorator for when a new message is received
@cl.on_message
async def handle_message(message:  cl.Message):
    # Get the message content from user
    prompt = message.content

    # Generate response using Gemini model
    response = model.generate_content(prompt)

    # Extract text from response, or empty string if no text attribute
    response_text = response.text if hasattr(response, "text") else ""
    
    # Send response back to user
    await cl.Message(content=response_text).send()