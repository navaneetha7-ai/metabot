from dotenv import load_dotenv
load_dotenv()

from metabot import MetaBot

bot = MetaBot(name="Mira", persona="friendly and helpful assistant")

print("Mira ready! Type 'exit' to quit.")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    reply = bot.chat(user)
    print(f"Mira: {reply}")