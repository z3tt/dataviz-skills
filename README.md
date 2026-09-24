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
| **advanced-ggplot2** | Publication-ready plots with ggplot2: coding conventions, theming, palettes, annotations, maps, export, and a mandatory verification pipeline (contrast, colorblind, grayscale) |
| **web-dataviz** | HTML-driven interactive visualizations: plain HTML+D3 boilerplate, SCSS structure, Svelte setup, scrollytelling (IntersectionObserver/scrollama), embedding, a11y & deployment |
| **quarto-reporting** | Branded Quarto documents via `_brand.yml`: project setup, brand colors/typography, figures with alt text, cross-references, publishing |
| **dataviz-workflow** | Project setup & tracking: change-tracking notepad, directory scaffold, and pre-build briefs (technical & theoretical) |
| **ggplot2-uncharted-drafter** | Internal skill for drafting lessons of the ggplot2 [un]charted course in `.tsx` (house style, components, exercises) |

## How they fit together

The toolkit covers the full lifecycle of a dataviz piece. Typical flows:

- **Static chart/report**: `dataviz-workflow` (brief + notepad) → `dataviz-principles` (design decisions) → `advanced-ggplot2` (implementation) → verification per skill
- **Branded deliverable**: add `quarto-reporting` (document, brand.yml, publishing) with figures built per `advanced-ggplot2`
- **Interactive piece**: `dataviz-principles` → `web-dataviz` (D3/ECharts/Svelte, scrollytelling, deployment)
- **Course lesson**: `ggplot2-uncharted-drafter` alone (course repo required)

Principles of the toolkit:
- **Suggestions, not laws** — every rule has a documented escape hatch when reasoning is valid and it improves storytelling and readability
- **Honesty across the spectrum** — from analytical to expressive, real data and honest framing are non-negotiable
- **Reasoning lives in `dataviz-principles`; mechanics live in the tool skills** — cross-referenced, never duplicated

## Install

```bash
git clone https://github.com/z3tt/dataviz-skills.git

# e.g. for Claude Code:
mkdir -p ~/.claude/skills/dataviz-principles
cp dataviz-skills/dataviz-principles/SKILL.md ~/.claude/skills/dataviz-principles/
```

## Usage notes

- `dataviz-principles` works in **any** AI tool — it contains no code rules.
- `advanced-ggplot2` works in any code-capable assistant working in R.
- `web-dataviz` works in any assistant that can write and ship web code.
- `quarto-reporting` and `dataviz-workflow` are tool-agnostic markdown workflows.
- `ggplot2-uncharted-drafter` is only useful with access to the course repo.

## License

[MIT](LICENSE) — free to use, adapt, and redistribute.
