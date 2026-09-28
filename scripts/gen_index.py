#!/usr/bin/env python3
"""扫描 topics/ concepts/ books/ 下的 .md 文档，读取 front-matter，
重新生成 README.md 中 <!-- INDEX:START --> 与 <!-- INDEX:END --> 之间的话题索引表。

用法：python3 scripts/gen_index.py
约定：每篇内容文档头部必须有 front-matter（title/date/type/confidence），
     没有 front-matter 或没有 date 的文档不会进入索引。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
DIRS = ["concepts", "books", "topics"]
START = "<!-- INDEX:START -->"
END = "<!-- INDEX:END -->"
TYPE_ORDER = {"概念": 0, "书籍": 1, "专题": 2}


def parse_front_matter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fm[key.strip()] = value.strip().strip('"')
    return fm


def first_h1(text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def build_rows() -> list:
    rows = []
    for d in DIRS:
        for f in sorted((ROOT / d).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            fm = parse_front_matter(text)
            if not fm.get("date"):
                continue
            rows.append({
                "date": fm.get("date", ""),
                "type": fm.get("type", ""),
                "title": fm.get("title") or first_h1(text) or f.stem,
                "path": f"{d}/{f.name}",
                "conf": fm.get("confidence", "-"),
            })
    # 先按类型稳定排序，再按日期倒序（利用 sorted 的稳定性）
    rows.sort(key=lambda r: TYPE_ORDER.get(r["type"], 9))
    rows.sort(key=lambda r: r["date"], reverse=True)
    return rows


def build_table(rows: list) -> str:
    lines = [
        "| 日期 | 类型 | 主题 | 文档 | 置信度 |",
        "|------|------|------|------|--------|",
    ]
    for r in rows:
        lines.append(
            f'| {r["date"]} | {r["type"]} | {r["title"]} '
            f'| [{r["path"]}]({r["path"]}) | {r["conf"]} |'
        )
    return "\n".join(lines)


def main() -> None:
    readme = README.read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        sys.exit(f"README.md 缺少 {START} / {END} 标记")
    rows = build_rows()
    table = build_table(rows)
    pre, rest = readme.split(START, 1)
    _, post = rest.split(END, 1)
    README.write_text(pre + START + "\n" + table + "\n" + END + post, encoding="utf-8")
    print(f"索引已更新：{len(rows)} 条")


if __name__ == "__main__":
    main()
