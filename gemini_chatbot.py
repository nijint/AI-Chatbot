import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-lite-latest")
chat = model.start_chat(history=[])

# IMPORTANT: this function will be used by the UI
def ask_bot(message):
    try:
        response = chat.send_message(message)
        return response.text
    except:
        return "Error or quota limit"

# keep terminal mode optional
if __name__ == "__main__":
    print("Chatbot ready\n")
    while True:
        user = input("You: ")
        if user.lower() == "quit":
            break
        print("Bot:", ask_bot(user))

