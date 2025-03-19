import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GENAI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

while True:
    user_input = input("\nEnter your question (or 'q' to exit): ")
    if user_input.lower() == "q":
        print("Thanks for chatting! Good bye!")
        break
    else:
        response = model.generate_content(user_input)
        print(response.text)