from google import genai

client = genai.Client(api_key="useap key")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say Hello"
)

print(response.text)
