import streamlit as st
import json
from datetime import datetime
from metabot import MetaBot

st.set_page_config(
    page_title="MetaBot",
    page_icon="🤖",
    layout="wide"
)

PERSONAS = {
    "🌸 Mira — Friendly": "friendly, warm and helpful assistant",
    "🧑‍🏫 Alex — Teacher": "patient teacher who explains step by step",
    "💼 Max — Professional": "professional and precise business assistant",
    "😄 Zara — Funny": "witty and humorous assistant who loves jokes",
    "🇮🇳 Tamil Bot": "assistant who always replies in Tamil language",
}

with st.sidebar:
    st.title("🤖 MetaBot")
    st.success("● Online")
    st.divider()
    st.subheader("Persona")
    selected = st.selectbox("Choose", list(PERSONAS.keys()))
    st.divider()
    st.subheader("Stats")
    msgs = st.session_state.get("messages", [])
    col1, col2 = st.columns(2)
    col1.metric("Messages", len(msgs))
    col2.metric("Replies", len([m for m in msgs if m["role"] == "assistant"]))
    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pop("bot", None)
        st.rerun()
    if st.button("💾 Save Chat", use_container_width=True):
        if len(msgs) == 0:
            st.warning("No messages to save!")
        else:
            filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(msgs, f, indent=2, ensure_ascii=False)
            st.success(f"Saved! {filename}")

if "selected" not in st.session_state or st.session_state.selected != selected:
    st.session_state.selected = selected
    st.session_state.messages = []
    bot_name = selected.split("—")[1].strip().split(" ")[0]
    st.session_state.bot = MetaBot(
        name=bot_name,
        persona=PERSONAS[selected]
    )

if "bot" not in st.session_state:
    bot_name = selected.split("—")[1].strip().split(" ")[0]
    st.session_state.bot = MetaBot(
        name=bot_name,
        persona=PERSONAS[selected]
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 MetaBot — Human AI Interaction")
st.caption("Powered by Ollama — Running locally on your PC")
st.divider()

if len(st.session_state.messages) == 0:
    st.info("👋 Hi! Select a persona from sidebar and start chatting!")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        reply_box = st.empty()
        full_reply = ""
        for chunk in st.session_state.bot.chat(user_input):
            full_reply += chunk
            reply_box.write(full_reply)
        reply = full_reply

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })