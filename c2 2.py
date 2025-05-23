from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Track collected data in a simple session dict (in-memory for demo)
user_data = {}

@app.route('/')
def home():
    return send_file('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        session_id = request.json.get("session_id", "default")

        if session_id not in user_data:
            user_data[session_id] = []

        history = user_data[session_id]
        history.append({"role": "user", "content": user_message})
        url = "https://query-mb0lwayy-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4.1/chat/completions?api-version=2025-01-01-preview"
        headers = {
            "Authorization": "Bearer FsXwuKVKc1bADM3BjvUGP0ypTAp2ylK17yGQfuvyPnCFkYQbAPreJQQJ99BEACHYHv6XJ3w3AAAAACOGb8Ml",  # Replace with your actual key
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-4",
            "messages": [{"role": "system", "content": "You are a helpful assistant."}] + history,
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()

        bot_reply = response_data["choices"][0]["message"]["content"]
        history.append({"role": "assistant", "content": bot_reply})

        return jsonify({"response": bot_reply})
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({"response": "I apologize, but I'm having trouble processing your request. Please try again."}), 500

if __name__ == "__main__":
    app.run(debug=True)