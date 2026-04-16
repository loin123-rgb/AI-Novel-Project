from __future__ import annotations

from pathlib import Path

from app.models import ChapterJob
from app.providers.base import BaseProvider


def read_md(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_md(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_prompt(root: Path, job: ChapterJob) -> str:
    return "\n\n".join(
        [
            read_md(root / "prompts" / "gemini_chapter_draft.md"),
            "# style_guide.md\n" + read_md(root / "style_guide.md"),
            "# story_state.md\n" + read_md(root / "state" / "story_state.md"),
            "# chapter_outline.md\n" + read_md(job.outline_path),
        ]
    )


def run_novel_draft(root: Path, provider: BaseProvider, job: ChapterJob) -> Path:
    prompt = build_prompt(root, job)
    content = provider.generate(prompt)
    output_path = root / "chapters" / f"{job.chapter_id}_draft.md"
    write_md(output_path, content)
    return output_path
