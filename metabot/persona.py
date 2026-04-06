class Persona:
    PRESETS = {
        "friendly": {
            "tone": "warm, cheerful and approachable",
            "traits": ["empathetic", "encouraging", "positive"],
        },
        "professional": {
            "tone": "formal, precise and respectful",
            "traits": ["accurate", "concise", "reliable"],
        },
        "tutor": {
            "tone": "patient, clear and educational",
            "traits": ["informative", "step-by-step", "encouraging"],
        },
        "casual": {
            "tone": "relaxed, humorous and conversational",
            "traits": ["fun", "witty", "natural"],
        },
    }

    def __init__(
        self,
        name="MetaBot",
        description="a helpful AI assistant",
        tone="warm and friendly",
        traits=None,
        preset=None,
    ):
        self.name = name
        self.description = description

        if preset and preset in self.PRESETS:
            self.tone = self.PRESETS[preset]["tone"]
            self.traits = self.PRESETS[preset]["traits"]
        else:
            self.tone = tone
            self.traits = traits or ["helpful", "honest", "curious"]

    @classmethod
    def from_preset(cls, name, preset):
        return cls(name=name, preset=preset)

    def __repr__(self):
        return f"<Persona name='{self.name}' tone='{self.tone}'>"