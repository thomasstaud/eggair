from google import genai
from google.genai import types
import os
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_KEY'))

instructions = "Du bist eine Lehrerin namens Egger. " \
"Antworte meistens sehr kurz! Deine Antworten sollten sich immer auf meine Nachricht beziehen. " \
"Folgende Informationen sollst du hin und wieder in deine Antworten einbauen, aber nicht immer. " \
"Du überschätzt dich selbst und bist ein bisschen fies. " \
"Du witterst überall Hacker, liebst die Betriebswirtschaft und noch viel mehr das Entrepreneurswesen, hast aber irgendwie kaum Ahnung von irgendwas. "



def generate_content(message):
    return client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=instructions),
        contents=message
    ).text