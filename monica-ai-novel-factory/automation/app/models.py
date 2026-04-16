from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ChapterJob:
    chapter_id: str
    outline_path: Path


@dataclass
class DraftResult:
    chapter_id: str
    content: str
