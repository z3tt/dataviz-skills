# dataviz-skills 📊

Reusable AI **skill files** for data visualization — distilled from the
[ggplot2 [un]charted](https://www.ggplot2-uncharted.com) course and years of
publication-grade dataviz practice.

Each skill is a plain `SKILL.md` with YAML frontmatter, following the
widely adopted agent-skills convention. Drop them into any AI provider that
supports skills (Claude Code: `.claude/skills/`, Vibe, Cursor, …) or paste
them into a system prompt.

## Skills

| Skill | Scope |
|---|---|
| **dataviz-principles** | Tool-agnostic design principles: chart choice, color semantics, titles, layout, honesty — no code |
| **advanced-ggplot-2** | Publication-ready ggplot2/R: coding conventions, theming, palettes, annotations, maps, export, and a mandatory verification pipeline (contrast, colorblind, grayscale) |
| **ggplot2-uncharted-drafter** | Internal skill for drafting lessons of the ggplot2 [un]charted course in `.tsx` (house style, components, exercises) |

## Install

```bash
git clone https://github.com/z3tt/dataviz-skills.git

# e.g. for Claude Code:
mkdir -p ~/.claude/skills/dataviz-principles
cp dataviz-skills/dataviz-principles/SKILL.md ~/.claude/skills/dataviz-principles/
```

## Usage notes

- `dataviz-principles` works in *any* AI tool — it contains no code.
- `advanced-ggplot-2` works in any code-capable assistant working in R.
- `ggplot2-uncharted-drafter` is only useful with access to the course repo.

## License

[MIT](LICENSE) — free to use, adapt, and redistribute.
