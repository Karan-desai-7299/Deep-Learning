from google import genai

client = genai.Client(api_key="AQ.Ab8RN6I_4ziMAL-ODtLVNqQHSwZalx1d2eYjSelosNNhEigYjg")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say Hello"
)

print(response.text)