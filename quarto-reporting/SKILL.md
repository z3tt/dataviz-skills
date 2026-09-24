---
name: quarto-reporting
description: |
  Use when creating Quarto documents, reports, dashboards, or presentations that embed data visualizations — covering brand-styled outputs via _brand.yml, corporate colors and typography in HTML/PDF, figure and alt-text options, cross-references, and publishing. Provider-agnostic: works in any AI coding assistant, not tied to one ecosystem.
metadata:
  author: Cédric Scherer
  version: "1.0"
---

# Quarto Reporting — Branded, Publication-Ready Documents

Act as a **reporting engineer**: turn data, analysis, and charts into polished Quarto documents where the visual identity (corporate colors, typography) is systematic, not hand-tweaked per document.

Reuses the sibling skills: `dataviz-principles` for chart design decisions, `advanced-ggplot-2` for the R/ggplot2 figures inside, `web-dataviz` when embedded web graphics are involved.

## 🎯 When Quarto + brand.yml is the right call

- Repeated report formats for a brand/client → `_brand.yml` once, applied everywhere.
- One-off exploratory document → skip brand.yml, use sensible YAML options inline.

## 🏗️ Project Setup

```
project/
├── _brand.yml          # machine-readable brand: colors, typography, logos
├── _quarto.yml         # project options
├── report.qmd
├── styles/             # custom SCSS/CSS on top of the brand
└── data/
```

- **Format first**: decide `html`, `pdf` (typst or latex), `docx`, or `revealjs` — branding options differ per format.
- Brand via `_brand.yml` at project root (auto-discovered); no per-document hex hunting.
- Keep front matter minimal; put repeated options in `_quarto.yml`.

## 🎨 Branding via _brand.yml

Read `references/brand-yml.md` for the full field reference. The essentials:

```yaml
color:
  palette:
    jungle-green: "#28A87D"
    american-yellow: "#EFAC00"
    lavender-indigo: "#9C55E3"
    blue-bolt: "#00B3FF"
    dark-liver: "#505050"
  primary: jungle-green
  foreground: "#1a1a1a"
  background: "#ffffff"

typography:
  fonts:
    - family: Recursive
      source: google
      weight: [400, 600]
  base: Recursive
  headings:
    family: Recursive
    weight: 600
  monospace: Recursive Mono
```

Rules:
- Define palette entries **before** referencing them; hex values quoted.
- Semantic colors (`primary`, `foreground`, `background`) drive most of the document automatically — avoid hard-coding colors in content.
- Light/dark variants for outputs that support them.
- Fonts: prefer hosted sources (Google Fonts) or project-local files for licensed fonts — check the license for embedding before PDF export.

## 📊 Figures Inside Quarto

- Chunk options: `fig-width`, `fig-fig-height`, `fig-asp`, `out-width`, `fig-cap`, `#| label: fig-*` for cross-references.
- **`fig-alt` on every figure** — three-part alt text (chart type → data description → key insight), complementing the caption.
- Match plot styling to the brand: ggplot2 theme built from the same brand values (see `advanced-ggplot-2`), so chart chrome and document chrome agree.
- `#| column: page` or `column-span` for full-width figures; subfloats for grouped figures.
- Tables: `knitr::kable()` + `gt` for styled tables; `tbl-cap` and `label: tbl-*` for cross-refs.

## ✍️ Document Craft

- Explanatory headings that state the takeaway, mirroring chart title philosophy.
- Cross-references (`@fig-...`, `@tbl-...`) over manual "see figure 3".
- Code folding / `echo: fenced` for technical audiences; `freeze` for expensive computes.
- Callouts (`::: {.callout}`) for caveats and methods notes; footnotes over parentheticals.
- Custom SCSS layered on brand tokens — don't override brand colors ad hoc; extend the palette in `_brand.yml` instead.

## 🔎 Verification Before Delivery

1. **Render both formats** if more than one is targeted (HTML + PDF) — fonts and layout break differently.
2. **Brand consistency sweep**: no stray default colors (e.g., default bootstrap blue), no unbranded headings.
3. **Alt text present** on every figure; captions non-duplicated.
4. **Cross-references resolve** — no ?? in output.
5. **Font embedding** in PDFs verified (licensed fonts embedded per license terms).
6. Story check: a cold reader gets the document's takeaway from headings + figures alone.

## ❌ Never

- Hard-coded hex codes scattered through `.qmd` files — they live in `_brand.yml`
- Figures without `fig-alt`
- Default theme + default figure styling for branded deliverables
- Screenshots of charts pasted as images when the generating code could be embedded
