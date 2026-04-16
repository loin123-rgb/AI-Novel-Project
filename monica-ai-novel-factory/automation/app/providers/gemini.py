from __future__ import annotations

from .base import BaseProvider


class GeminiProvider(BaseProvider):
    def __init__(self, model: str) -> None:
        self.model = model

    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Implement Gemini API call here.")
