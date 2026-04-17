from __future__ import annotations

from .base import BaseProvider


class GeminiProvider(BaseProvider):
    def __init__(self, model: str, api_key: str) -> None:
        self.model = model
        self.api_key = api_key

    def generate(self, prompt: str) -> str:
        try:
            from google import genai
        except ImportError as exc:
            raise RuntimeError(
                "google-genai is not installed. Run `pip install google-genai` first."
            ) from exc

        client = genai.Client(api_key=self.api_key)
        response = client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        text = getattr(response, "text", None)
        if text:
            return text.strip()

        raise RuntimeError("Gemini response did not contain text output.")
