from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    try:
        question = request.form.get("question")

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question
        )

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        print(e)
        return jsonify({
            "response": str(e)
        }), 500


@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        email = request.form.get("email")

        prompt = f"""
Summarize the following email in 2-3 sentences.

{email}
"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        print(e)
        return jsonify({
            "response": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)