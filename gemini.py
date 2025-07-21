from google import genai
import os
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_KEY'))



def generate_content(message):
    return client.models.generate_content(
        model="gemini-2.5-flash", contents=message
    )