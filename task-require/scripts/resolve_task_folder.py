#!/usr/bin/env python3
"""Resolve a task folder path from explicit input or the latest folder."""

import argparse
import sys
from pathlib import Path


def resolve_task_folder(project_root: Path, hint: str | None = None) -> Path:
    tasks_dir = project_root / ".codex" / "tasks"
    if not tasks_dir.exists():
        raise FileNotFoundError(f"Task directory does not exist: {tasks_dir}")

    if hint:
        candidate = Path(hint)
        if candidate.is_absolute() and candidate.exists():
            return candidate
        candidate = tasks_dir / hint
        if candidate.exists():
            return candidate
        raise FileNotFoundError(f"Task folder not found: {hint}")

    folders = sorted(
        [p for p in tasks_dir.iterdir() if p.is_dir()],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not folders:
        raise FileNotFoundError(f"No task folders found in {tasks_dir}")
    return folders[0]


def main():
    parser = argparse.ArgumentParser(description="Resolve task folder path.")
    parser.add_argument("project_root", help="Project root directory")
    parser.add_argument("hint", nargs="?", help="Task folder name or path (optional)")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    try:
        folder = resolve_task_folder(root, args.hint)
        print(folder)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
