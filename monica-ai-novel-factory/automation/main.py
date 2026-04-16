from __future__ import annotations

from pathlib import Path

from app.config import load_config


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    config = load_config(root)
    print("MONICA automation scaffold ready.")
    print(f"default_provider={config.default_provider}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
