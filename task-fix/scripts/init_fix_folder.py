#!/usr/bin/env python3
"""
Create a fix record file under <project-root>/.codex/fix/.

Usage:
  python3 init_fix_folder.py <project-root> "<fix-title>"

Outputs the path to the created fix-*.md file on stdout.
"""

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


def create_fix_file(project_root: Path, title: str) -> Path:
    fix_dir = project_root / ".codex" / "fix"
    fix_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%Y-%m-%d %H:%M")
    slug = slugify(title) or "bug-fix"
    filename = f"fix-{date_str}-{slug}.md"

    filepath = fix_dir / filename
    counter = 1
    while filepath.exists():
        filepath = fix_dir / f"fix-{date_str}-{slug}-{counter}.md"
        counter += 1

    filepath.write_text(
        f"""# 修复记录

**创建时间**: {time_str}
**状态**: 收集中
**修复会话**: {filepath.stem}

---

## Bug 列表

### BUG-001

- [ ] <!-- bug_id: BUG-001 / 提出时间: {time_str} -->
  **用户反馈**: <请描述 Bug 现象>
  **修复建议**: 待分析
  **修复方案**: 待分析
  **修复状态**: 待修复
  **验证结果**: -

---

## 修复进度总览

| Bug ID | 状态 | 完成时间 |
|--------|------|----------|
| BUG-001 | ⏳ 待修复 | - |

## 会话记录

| 时间 | 操作 | 备注 |
|------|------|------|
| {time_str} | 创建修复会话 | - |

## 恢复标记

last_processed_bug: BUG-001
last_action: created
""",
        encoding="utf-8",
    )

    return filepath


def main():
    parser = argparse.ArgumentParser(description="Create a new fix record file.")
    parser.add_argument("project_root", help="Project root directory")
    parser.add_argument("title", help="Short fix title / description")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    fpath = create_fix_file(root, args.title)
    print(fpath)


if __name__ == "__main__":
    main()
