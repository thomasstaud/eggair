from google import genai

client = genai.Client(api_key="AIzaSyBKQwlYd0j8gME1TsiCY7m1JBtuFCFWfe4")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)