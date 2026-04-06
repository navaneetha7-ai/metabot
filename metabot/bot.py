import requests
import json

class MetaBot:
    def __init__(
        self,
        name=" MetaBot ",
        persona="friendly, warm and helpful assistant",
    ):
        self.name = name
        self.persona = persona
        self.system = (
            f"You are {self.name}, {self.persona}. "
            f"Talk naturally like a human. "
            f"Keep responses short and conversational."
        )
        self.history = []

    def chat(self, user_input):
        self.history.append({
            "role": "user",
            "content": user_input
        })
        messages = [{"role": "system", "content": self.system}] + self.history

        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "phi3",
                "messages": messages,
                "stream": True
            },
            stream=True
        )

        full_reply = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                chunk = data.get("message", {}).get("content", "")
                full_reply += chunk
                yield chunk

        self.history.append({
            "role": "assistant",
            "content": full_reply
        })

    def reset(self):
        self.history = []
        print(f"{self.name}: Memory cleared!")