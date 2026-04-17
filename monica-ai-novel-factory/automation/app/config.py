from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


@dataclass
class AppConfig:
    root: Path
    default_provider: str = "gemini"
    gemini_api_key: str = field(default="")
    gemini_model: str = "gemini-2.5-flash-lite"
    ollama_base_url: str = "http://127.0.0.1:11434"
    ollama_model: str = "qwen2.5:7b"


def load_config(root: Path) -> AppConfig:
    return AppConfig(
        root=root,
        default_provider=os.getenv("DEFAULT_PROVIDER", "gemini"),
        gemini_api_key=os.getenv("GEMINI_API_KEY", ""),
        gemini_model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite"),
        ollama_base_url=os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434"),
        ollama_model=os.getenv("OLLAMA_MODEL", "qwen2.5:7b"),
    )
