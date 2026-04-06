import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

class MetaBot:
    def __init__(self, name="MetaBot", persona="Helpful assistant"):
        self.name = name
        self.persona = persona
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def chat(self, message):
        response = self.model.generate_content(
            f"{self.persona}\nUser: {message}"
        )
        return response.text