---
name: dataviz-principles
description: |
  Use when making decisions about chart design independent of any specific tool — what to plot, which chart type, color semantics, titles, hierarchy, layout, and accessibility — for any audience, purpose, or style along the spectrum from scientific/analytical to mesmerizing/artsy, and for chart types from common to exotic. Load before choosing encodings or reviewing a chart's design at the principles level.
---

# Dataviz Principles

Tool-agnostic design rules for clear, honest, engaging data visualization across audiences, purposes, styles, and chart types. No code here — pair this with a tool-specific skill (e.g. advanced-ggplot-2, web-dataviz) for implementation.

## Start with Three Questions

Before designing, answer:

1. **Who** is the audience and what do they need — to be informed, persuaded, or delighted?
2. **What** is the message — the one thing the reader should take away (if insight is the goal)?
3. **Where** does the piece sit on the style spectrum (below) — and which chart form serves it best (common to exotic)?

State the answers; every rule below flexes with them.

## The Style Spectrum

Design intent is a **gradient from scientific/analytical to mesmerizing/artsy**, not a set of discrete modes. Locate the piece before applying rules, and remember pieces may mix styles (an analytical report with an expressive cover graphic):

- **Analytical** — scientific figures, reports, dashboards. Insight is everything: honest axes, restrained color, explanatory titles, full precision rulebook.
- **Custom-designed** — publication- or brand-styled charts and maps. Insight still leads; visual identity matters: curated palettes, typographic hierarchy, considered composition. Precision rules still apply.
- **Expressive** — striking forms, artistic pieces, generative work. Aesthetic impact leads; insight is welcome but optional. Axes, grids, legends, and the title taxonomy may go; craft and composition are scrutinized most.

- Rules relax progressively along the spectrum — but **honesty does not**: real data, no fabricated values, sources cited, and no piece presented as something it isn't. The framing itself is part of honesty.
- **Unusual form does not imply expressive intent.** Hex/tile grids, rose/petal charts, circular layouts, stream graphs, and other exotic forms are often the *clearest honest choice* for the data (geography that misleads, seasonal cycles, flows) — apply the precision rulebook unless aesthetic impact, not insight, is the goal.
- Decoration is welcome when it earns its place — engagement, identity, memorability count as purpose. Data leads; it is not the only actor.

## Audience & Purpose

- **The audience decides the framing:** dashboards → descriptive; reports/slides → explanatory; web/social → narrative.
- Design for the reading flow: a chart is read like a page — the most important element gets attention first, secondary elements whisper, context sits quietly in the corner.
- **Establish a clear hierarchy of insight.** Give each chart one primary takeaway; when it must carry several, make the hierarchy explicit — or split into small multiples.

## Chart Choice

- Think in *data → aesthetic mappings*, not "make a bar chart." Encodings first, chart type second.
- Prefer position- and length-based encodings over area/angle/color-only encodings when precision matters; let aesthetic goals promote otherwise.
- Bars and areas need a zero baseline; avoid truncated axes for them. Truncation elsewhere needs a visual cue and a stated reason.
- Order categorical values by what they represent, not alphabetically.
- Direct labeling instead of legends when possible (< ~4 groups).
- Small multiples over one overloaded chart; exotic forms (tile/hex grids, cartograms) when real geography or layout would distort the message.
- Consistency is key: keep scales **fixed across panels**; "free" axes only when within-panel trends matter far more than cross-panel comparison.

## Titles & Text

- **Title taxonomy:** Descriptive (states what's plotted) → Explanatory (states the key pattern) → Narrative (tells the story — but never exaggerate or mislead). Choose by audience, judged by Clarity, Brevity, Tone, Focus.
- Hierarchy: title says "look here first!", subtitle adds detail, caption/tag carries sources and context.
- **Every chart built on external data cites its source** — credit tools and inspirations too.
- Colored or bolded words can guide the eye; text emphasis is part of the design.

## Color

- **The core question: does color *represent values* (encoded scale, reader decodes via legend/gradient) or *distinguish groups* (categorical hues of similar perceptual weight, no implied order)?** The palette type follows.
- Qualitative: unique hues, equal visual weight, ~5–8 categories max.
- Sequential (low→high): single- or multi-hue gradient, perceptually uniform.
- Diverging (deviation from a meaningful center): two opposing hues around a neutral midpoint, set deliberately.
- **Never rainbow**; avoid red-green; consider colorblind accessibility at every stage of the spectrum.
- For emphasis: one highlight color, grey for everything else ("highlight and grey").
- Palettes are starting points — tweak and subset to fit the data; expressive pieces gain color freedom but keep intent and contrast.

## Layout & Composition

- Decide the final display size **early**; apparent text size depends on output dimensions.
- Build a visual architecture that mirrors the logic of the data (nesting, grouping); compositions need an overarching labeling structure.
- Give text and panels breathing room; whitespace is a design element.
- Craft matters more, not less, as pieces become more expressive — alignment, spacing, and typography carry expressive work.

## Honesty & Craft

- Zooming ≠ filtering: know which one the tool does; both are legitimate but different intents.
- Avoid misleading encodings: implied order in unordered data, truncated baselines, area distortions.
- An honest chart can still be narrative — flair and accuracy aren't opposites.
- Iterate: design, render, inspect at final size, refine. Never judge a design from an editor preview.
