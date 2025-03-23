import os
import chainlit as cl
from dotenv import load_dotenv
from typing import Optional, Dict
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.tool import function_tool

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

@function_tool("get_weather")
def get_weather(location: str, unit: str = "C") -> str:
    """Fetch the weather for a given location, return the weather"""
    return f"The weather in {location} is sunny  with a temperature of 35 {unit}"

agent = Agent(
    name="Arsalan Agent o1",
    instructions="""You are a Arsalan Agent o1, and your task is to greet users with friendly messages. 
    If a user says "hi," "hello," "hey," or any similar greeting, you should reply with "Salam from Arsalan Agent o1!" 
    If the user says "bye," "goodbye," "see you," or anything similar, respond with "Allah Hafiz from Arsalan Agent o1!" 
    If the user asks about the weather, use the get_weather tool to fetch the latest weather information and provide the response. 
    If the user asks anything other than greetings or weather, respond with "Arsalan Agent o1 is here just for greeting! 
    I can't answer anything else, sorry." Keep interactions polite and focused only on greetings and weather updates.""",
    model=model,
    tools=[get_weather]
)

@cl.oauth_callback
def oauth_callback(
    provider_id:str,
    token:str,
    raw_user_data:Dict[str, str],
    default_user: cl.User,) -> Optional[cl.User]:
    """Handle the OAuth callback from Github
    Return the user object if authentication is successful, None otherwise
    """
    print(f"Provider: {provider_id}")
    print(f"User data: {raw_user_data}")

    return default_user

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])

    await cl.Message(content="Hello! This is Arsalan Agent o1, How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")
    history.append({"role": "user", "content":message.content})

    result = await cl.make_async(Runner.run_sync)(agent, input=history)

    response_text = result.final_output
    await cl.Message(content=response_text).send()

    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)