from __future__ import annotations

import argparse
from pathlib import Path

from app.config import load_config
from app.providers.gemini import GeminiProvider
from app.models import ChapterJob
from app.workflows.novel_workflow import run_novel_draft


def main() -> int:
    parser = argparse.ArgumentParser(prog="monica", description="MONICA AI Novel Factory")
    subparsers = parser.add_subparsers(dest="command", required=True)

    draft_parser = subparsers.add_parser("draft", help="Generate a chapter draft.")
    draft_parser.add_argument("chapter_id", help="Chapter ID, e.g. chapter_006")
    draft_parser.add_argument("outline", type=Path, help="Path to the chapter outline .md file")
    draft_parser.add_argument("--model", default=None, help="Override Gemini model")

    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    config = load_config(root)

    if args.command == "draft":
        if not config.gemini_api_key:
            print("ERROR: GEMINI_API_KEY is not set.")
            return 1

        model = args.model or config.gemini_model
        provider = GeminiProvider(model=model, api_key=config.gemini_api_key)
        job = ChapterJob(chapter_id=args.chapter_id, outline_path=args.outline)
        output_path = run_novel_draft(root=root, provider=provider, job=job)
        print(f"Mode: gemini-api")
        print(f"Model: {model}")
        print(f"Draft: {output_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
