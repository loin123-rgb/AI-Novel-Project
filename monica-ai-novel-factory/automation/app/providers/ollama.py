from __future__ import annotations

from .base import BaseProvider


class OllamaProvider(BaseProvider):
    def __init__(self, base_url: str, model: str) -> None:
        self.base_url = base_url
        self.model = model

    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Implement Ollama fallback here.")
