import requests
import json
from src.core.base import LLMProvider

class OllamaProvider(LLMProvider):
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3"):
        self.url = f"{base_url}/api/chat"
        self.model = model

    def chat(self, prompt: str, system_prompt: str = "") -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
        response = requests.post(self.url, json=payload)
        return response.json().get('message', {}).get('content', '')
