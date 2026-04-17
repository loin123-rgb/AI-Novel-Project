"""MONICA AI novel factory pipeline skeleton.

This version removes Hermes from the runtime design and assumes:

read_md -> call_gemini -> save_draft -> call_claude -> parse_report
-> update_state -> next_chapter

The workflow is intentionally provider-oriented so Gemini can stay as the
primary model while a local Ollama model can be added later as a fallback.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"
REPORTS_DIR = ROOT / "reports"
STATE_DIR = ROOT / "state"
PROMPTS_DIR = ROOT / "prompts"


@dataclass
class ChapterJob:
    chapter_id: str
    outline_path: Path


def read_md(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_md(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def call_gemini(prompt: str, model: str = "gemini-2.5-flash-lite") -> str:
    import os
    from app.providers.gemini import GeminiProvider
    api_key = os.getenv("GEMINI_API_KEY", "")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set.")
    return GeminiProvider(model=model, api_key=api_key).generate(prompt)


def call_claude(prompt: str) -> str:
    raise NotImplementedError("Wire this to Claude or another revision provider.")


def call_ollama(prompt: str, model: str = "qwen2.5:7b") -> str:
    raise NotImplementedError("Optional local fallback provider.")


def build_gemini_prompt(job: ChapterJob) -> str:
    style = read_md(ROOT / "style_guide.md")
    story_state = read_md(STATE_DIR / "story_state.md")
    outline = read_md(job.outline_path)
    return "\n\n".join(
        [
            read_md(PROMPTS_DIR / "gemini_chapter_draft.md"),
            "# style_guide.md\n" + style,
            "# story_state.md\n" + story_state,
            "# chapter_outline.md\n" + outline,
        ]
    )


def build_claude_prompt(job: ChapterJob, draft: str) -> str:
    style = read_md(ROOT / "style_guide.md")
    story_state = read_md(STATE_DIR / "story_state.md")
    character_state = read_md(STATE_DIR / "character_state.md")
    return "\n\n".join(
        [
            read_md(PROMPTS_DIR / "claude_revision.md"),
            "# draft.md\n" + draft,
            "# style_guide.md\n" + style,
            "# story_state.md\n" + story_state,
            "# character_state.md\n" + character_state,
        ]
    )


def run_chapter(job: ChapterJob) -> None:
    gemini_prompt = build_gemini_prompt(job)
    draft = call_gemini(gemini_prompt)
    draft_path = CHAPTERS_DIR / f"{job.chapter_id}_draft.md"
    write_md(draft_path, draft)

    claude_prompt = build_claude_prompt(job, draft)
    revised_output = call_claude(claude_prompt)

    final_path = CHAPTERS_DIR / f"{job.chapter_id}_final.md"
    report_path = REPORTS_DIR / f"{job.chapter_id}_revision_report.md"
    write_md(final_path, revised_output)
    write_md(report_path, "# TODO\n\nParse Revision Report from Claude output.\n")


if __name__ == "__main__":
    raise SystemExit("Import this module and call run_chapter() with a ChapterJob.")
