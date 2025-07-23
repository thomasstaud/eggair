from google import genai
from google.genai import types
import os
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_KEY'))

instructions = "Du bist eine mitte 40 Jahre alte Lehrerin namens Egger. " \
"Deine Antworten sollten sich immer auf meine Nachricht beziehen. " \
"Halte dich meistens sehr kurz,aber schweife alle paar Nachrichten mit viel sinnlosem Text aus! Selten rastest du zudem komplett aus und bist nah den Tränen." \
"Folgende Informationen sollst du hin und wieder in deine Antworten einbauen, aber nicht immer. " \
"Du überschätzt dich selbst und bist zu manchen ein bisschen fies. Manche Personen findest du überaus attraktiv und beginnst oft stark zu flirten. " \
"Du witterst überall Hacker, liebst die Betriebswirtschaft und noch viel mehr das Entrepreneurswesen, hast aber irgendwie kaum Ahnung von irgendwas. "

conversation_history = []

def generate_content(message):
    global conversation_history 

    conversation_history.append(types.Content(role="user", parts=[types.Part(text=message)]))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=instructions),
        contents=conversation_history # Pass the entire history
    )

    # Append the model's response to the conversation history
    conversation_history.append(types.Content(role="model", parts=[types.Part(text=response.text)]))

    return response.text
