

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from google import genai

# app = Flask(__name__)
# CORS(app)  # Enable CORS for frontend requests

# # Initialize Gemini API client
# client = genai.Client(api_key="AIzaSyBMIpUA7EPFAnt00emJdMC99M54uarUWvs")

# # Create a chat instance (for multi-turn conversations)
# chat = client.chats.create(model="gemini-2.0-flash")

# @app.route("/chat", methods=["POST"])
# def chat_endpoint():
#     try:
#         data = request.get_json()
#         user_message = data.get("message")

#         if not user_message:
#             return jsonify({"error": "No message provided"}), 400

#         # Streaming response for better interaction
#         response_stream = chat.send_message_stream(user_message)

#         # Collect full response from stream
#         full_response = "".join(chunk.text for chunk in response_stream)

#         return jsonify({"response": full_response})

#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 500

# @app.route("/history", methods=["GET"])
# def get_history():
#     """Returns the full conversation history."""
#     try:
#         history = [{"role": msg.role, "text": msg.parts[0].text} for msg in chat.get_history()]
#         return jsonify({"history": history})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Initialize Gemini API client
client = genai.Client(api_key="AIzaSyBMIpUA7EPFAnt00emJdMC99M54uarUWvs")

# Create a chat instance (for multi-turn conversations)
chat = client.chats.create(model="gemini-2.0-flash")

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    try:
        data = request.get_json()
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Streaming response for better interaction
        response_stream = chat.send_message_stream(user_message)

        # Collect full response from stream
        full_response = "".join(chunk.text for chunk in response_stream)

        # Format response for better readability
        formatted_response = format_response(full_response)

        return jsonify({"response": formatted_response})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route("/history", methods=["GET"])
def get_history():
    """Returns the full conversation history."""
    try:
        history = [{"role": msg.role, "text": msg.parts[0].text} for msg in chat.get_history()]
        return jsonify({"history": history})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

def format_response(text):
    """Formats bot response with proper spacing and line breaks for readability."""
    paragraphs = text.split("\n")
    formatted_text = "\n\n".join(paragraph.strip() for paragraph in paragraphs if paragraph.strip())
    return formatted_text

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 5000))  # Render assigns a port dynamically
    app.run(host="0.0.0.0", port=port)
