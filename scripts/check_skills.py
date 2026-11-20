#!/usr/bin/env python3
"""Lint skill files in a skills repo (stdlib only).

Checks every */SKILL.md:
- `name` is an inline scalar matching ^[a-z0-9-]+$ and equal to the directory
  name. Block-scalar names (name: |) parse with a trailing newline and fail
  the pattern in some CLIs (e.g. Vibe) — keep `name` inline.
- `description` is present, a string, and <= 1024 chars. Block scalars
  (description: |) are fine here: they parse to a plain string.
- `metadata` with `author` and `version` is present.

Also scans markdown files for references to skill-like tokens (backticked or
*emphasized*) that closely resemble a real skill directory name but do not
match it — catches stale names after renames.

Usage: python3 scripts/check_skills.py [repo_root]   (default: cwd)
Exit code 0 = clean, 1 = problems found.
"""
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9-]+$")
TOKEN_RE = re.compile(r"\b[a-z0-9]+(?:-[a-z0-9]+)+\b")
URL_RE = re.compile(r"https?://\S+")
MAX_DESC = 1024


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 4:]


def check_skill(path, errors):
    text = path.read_text(encoding="utf-8")
    fm, _body = split_frontmatter(text)
    if fm is None:
        errors.append(f"{path}: missing frontmatter")
        return
    lines = fm.split("\n")

    m = re.search(r"^name:\s*(.*)$", fm, re.M)
    if not m:
        errors.append(f"{path}: no name field")
    else:
        raw = m.group(1).strip()
        if raw in ("|", ">", "|-", ">-", "|+", ">+"):
            errors.append(f"{path}: name must be an inline scalar, not a block scalar (parses with trailing newline, fails ^[a-z0-9-]+$ in some CLIs)")
        elif not NAME_RE.match(raw):
            errors.append(f"{path}: name {raw!r} fails ^[a-z0-9-]+$")
        elif raw != path.parent.name:
            errors.append(f"{path}: name {raw!r} != directory {path.parent.name!r}")

    dm = re.search(r"^description:\s*([|>][+-]?)?\s*$", fm, re.M)
    if dm and dm.group(1):
        body = []
        started = False
        for line in lines:
            if line.startswith("description:"):
                started = True
                continue
            if started:
                if line.startswith("  ") or line == "":
                    body.append(line.strip())
                else:
                    break
        desc = " ".join(b for b in body if b)
    else:
        im = re.search(r"^description:\s*(.+)$", fm, re.M)
        desc = im.group(1).strip() if im else ""
    if not desc:
        errors.append(f"{path}: empty description")
    elif len(desc) > MAX_DESC:
        errors.append(f"{path}: description {len(desc)} chars > {MAX_DESC}")

    mm = re.search(r"^metadata:\s*$", fm, re.M)
    if not mm:
        errors.append(f"{path}: missing metadata block")
    else:
        meta = fm[mm.end():]
        meta = meta.split("\n---")[0]
        if not re.search(r"^  author:\s*\S+", meta, re.M):
            errors.append(f"{path}: metadata missing author")
        if not re.search(r'^  version:\s*"?[0-9]', meta, re.M):
            errors.append(f"{path}: metadata missing version")


def check_refs(root, skill_names, errors):
    md_files = [p for p in root.rglob("*.md") if ".git" not in p.parts]
    for p in md_files:
        text = URL_RE.sub(" ", p.read_text(encoding="utf-8"))
        for tok in set(TOKEN_RE.findall(text)):
            if tok in skill_names or "/" in tok:
                continue
            close = max(skill_names, key=lambda s: SequenceMatcher(None, tok, s).ratio())
            ratio = SequenceMatcher(None, tok, close).ratio()
            if ratio >= 0.8:
                errors.append(f"{p}: reference {tok!r} looks like stale skill name (closest: {close!r}, ratio {ratio:.2f})")


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    skills = sorted(p for p in root.glob("*/SKILL.md"))
    if not skills:
        print(f"no */SKILL.md under {root}")
        return 1
    errors = []
    for p in skills:
        check_skill(p, errors)
    check_refs(root, {p.parent.name for p in skills}, errors)
    if errors:
        print(f"{len(errors)} problem(s) in {root}:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {len(skills)} skills clean under {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
