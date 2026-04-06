EMOTION_KEYWORDS = {
    "happy": ["happy", "great", "awesome", "love", "excellent", "amazing", "joy", "excited"],
    "sad": ["sad", "unhappy", "depressed", "miss", "lonely", "cry", "upset", "down"],
    "angry": ["angry", "mad", "furious", "annoyed", "frustrated", "hate", "rage"],
    "confused": ["confused", "dont understand", "what", "unclear", "lost", "huh", "how"],
    "anxious": ["worried", "nervous", "anxious", "scared", "fear", "stress", "panic"],
    "neutral": [],
}

def detect_emotion(text):
    text_lower = text.lower()
    for emotion, keywords in EMOTION_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            return emotion
    return "neutral"

def format_response(name, text):
    return f"{name}: {text}"

def truncate(text, max_chars=500):
    return text if len(text) <= max_chars else text[:max_chars] + "..."

def count_tokens_approx(text):
    return len(text) // 4