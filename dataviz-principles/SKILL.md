---
name: |
  dataviz-principles
description: |
  Use when making decisions about chart design independent of any specific tool — what to plot, which chart type, color semantics, titles, hierarchy, layout, and accessibility — for analytical charts and data-art pieces alike. Load before choosing encodings or reviewing a chart's design at the principles level.
---

# Dataviz Principles

Tool-agnostic design rules for clear, honest, publication-quality data visualization — covering both analytical charts and expressive data art. No code here — pair this with a tool-specific skill (e.g. advanced-ggplot-2, web-dataviz) for implementation.

## First Principles

- **Every visual element must represent data.** Remove anything decorative that doesn't serve a purpose.
- **One insight per chart.** If it feels crowded, split into small multiples.
- **Order categorical values by what they represent**, not alphabetically.
- **The audience decides:** dashboards → descriptive; reports/slides → explanatory; web/social → narrative.
- Design for the reading flow: people read a chart like a page — the most important element gets attention first, secondary elements whisper, context sits quietly in the corner.

## Chart Choice

- Pick encodings before chart types: think in *data → aesthetic mappings*, not "make a bar chart".
- Bars need a zero baseline; avoid truncated axes for bar/area charts.
- Use direct labeling instead of legends when possible (< ~4 groups).
- Prefer position- and length-based encodings over area/angle/color-only encodings.
- Small multiples over one overloaded chart; tile/hex-grid maps when real geography distorts the message.

## Titles & Text Hierarchy

- **Title taxonomy**: Descriptive (states what's plotted — technically correct, no insight) → Explanatory (states the key pattern — clear but long) → Narrative (tells the story, memorable — but never exaggerate or mislead).
- Judge titles by **Clarity, Brevity, Tone, Focus**.
- Hierarchy: title says "look here first!", subtitle adds detail, caption/tag carries sources and context.
- **Every chart built on external data cites its source** — credit tools and inspirations too.
- Colored or bolded words can guide the eye; text emphasis is part of the design.

## Color

- **The core question: does color *represent values* or *distinguish groups*?**
  - Represent values → an encoded scale the reader must decode (legend/gradient).
  - Distinguish groups → categorical hues of **similar perceptual weight**, no implied order.
- Categorical/qualitative: unique hues, equal visual weight, max 5–8 categories.
- Sequential (low→high): single- or multi-hue gradient.
- Diverging (deviation from a meaningful center): two opposing hues around a neutral midpoint; set the midpoint deliberately.
- **Never rainbow**; avoid red-green; prefer perceptually uniform families when in doubt; always consider colorblind accessibility.
- For emphasis: one highlight color, grey for everything else ("highlight and grey").
- Palettes are starting points — tweak and subset to fit the data.

## Layout & Composition

- Keep scales **consistent (fixed) across panels**; "free" axes only when within-panel trends matter far more than cross-panel comparison.
- Build a visual architecture that mirrors the logic of the data (nesting, grouping).
- Composition needs an overarching labeling structure (tags, shared titles).
- Decide the final display size **early**; apparent text size depends on output dimensions.
- Give text and panels breathing room; whitespace is a design element.

## The Dataviz Spectrum: Analytical → Custom → Abstract

Chart design is a **gradient, not a binary**. Locate the piece on the spectrum before designing; every rule below flexes accordingly:

1. **Analytical** — default charts, scientific figures, reports. Insight is everything: full rulebook, honest axes, restrained color, explanatory titles.
2. **Custom-designed** — publication- or brand-styled charts and maps, poster-ready figures. Insight still leads, but visual identity matters: custom themes, curated palettes, typographic hierarchy, considered composition. Craft rules tighten; strict conventions (zero baselines, direct labeling) still apply.
3. **Abstract / data-art** — artistic, experimental, generative pieces. Aesthetic impact leads; insight is optional. Axes, grids, legends, and the title taxonomy may go; composition and typography are scrutinized most.

- **Not mutually exclusive** — pieces can sit between stages or mix them (e.g., a custom-designed scrollytelling piece with an abstract hero graphic). State where the piece sits rather than "choosing a mode."
- The further along the spectrum, the more precision rules relax — but **honesty never does**: real data, no fabricated values, sources cited. Each stage drops fewer rules than the next, and none drops integrity.
- Never present an abstract piece as an analytical one (and vice versa) — the framing itself is part of honesty.

## Honesty & Trust

- Zooming ≠ filtering: know which one your tool does; both are legitimate but different intents.
- Avoid misleading encodings (implied order in unordered data, truncated baselines, area distortions).
- An honest chart can still be narrative — flair and accuracy aren't opposites.
- Iterate: design, render, inspect at final size, refine. Never judge a design from an editor preview.
