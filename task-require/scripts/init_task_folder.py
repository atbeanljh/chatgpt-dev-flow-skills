#!/usr/bin/env python3
"""Create a new task folder under <project-root>/.codex/tasks/."""

import argparse
import re
from datetime import datetime
from pathlib import Path


def slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")[:40]


def create_task_folder(project_root: Path, title: str) -> Path:
    tasks_dir = project_root / ".codex" / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)

    date_prefix = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title) or "task"
    folder_name = f"{date_prefix}-{slug}"

    # Avoid collisions
    candidate = tasks_dir / folder_name
    counter = 1
    while candidate.exists():
        candidate = tasks_dir / f"{folder_name}-{counter}"
        counter += 1

    candidate.mkdir(parents=True, exist_ok=False)

    req_file = candidate / "01-requirements.md"
    req_file.write_text(
        f"""# 需求文档

## 任务基本信息
- 任务ID: {candidate.name}
- 创建日期: {datetime.now().strftime("%Y-%m-%d %H:%M")}
- 状态: 需求确认中

## 原始需求
{title}

## 需求澄清记录
| 问题 | 回答 |
|------|------|
| | |

## 功能需求
1.

## 非功能需求
1.

## 验收标准
1.

## 待确认问题
- [ ]
""",
        encoding="utf-8",
    )

    return candidate


def main():
    parser = argparse.ArgumentParser(description="Create a new task folder.")
    parser.add_argument("project_root", help="Project root directory")
    parser.add_argument("title", help="Short task title/description")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    folder = create_task_folder(root, args.title)
    print(folder)


if __name__ == "__main__":
    main()
