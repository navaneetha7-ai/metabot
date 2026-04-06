import json
import os
from datetime import datetime

class Memory:
    def __init__(self, max_turns=50, persist=False, file="memory.json"):
        self.max_turns = max_turns
        self.persist = persist
        self.file = file
        self.history = []

        if persist and os.path.exists(file):
            self._load()

    def add(self, role, content):
        self.history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })

        if len(self.history) > self.max_turns * 2:
            self.history = self.history[-(self.max_turns * 2):]

        if self.persist:
            self._save()

    def get_history(self):
        return [{"role": m["role"], "content": m["content"]} for m in self.history]

    def clear(self):
        self.history = []
        if self.persist and os.path.exists(self.file):
            os.remove(self.file)

    def _save(self):
        with open(self.file, "w") as f:
            json.dump(self.history, f, indent=2)

    def _load(self):
        with open(self.file, "r") as f:
            self.history = json.load(f)

    def summary(self):
        return f"Memory: {len(self.history)} messages stored"