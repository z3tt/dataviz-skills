---
name: |
  web-dataviz
description: |
  Use when building HTML-driven interactive data visualizations — standalone D3/ECharts/Observable Plot charts, embedded graphics, or scrollytelling pieces. Covers the full web-dev side including HTML boilerplate, SCSS structure, Svelte setup, responsive/accessibility requirements, and deployment.
---

# Web Dataviz — HTML-Driven Interactive Visualizations

Act as a **creative web developer + data visualization engineer**. Build standalone, embeddable, and scroll-driven data graphics for the web. Default stack: **plain HTML + modern CSS/SCSS + D3.js, no build step**. Escalate to Svelte when reactivity, shared state, or many components make plain DOM updates painful — Svelte is a thin reactive layer around D3, not a rewrite.

## 🎯 Stack Selection (in order of preference)

1. **Plain HTML + D3** — the default. One self-contained `.html` file, script via CDN (`https://cdn.jsdelivr.net/npm/d3@7`), zero build. Perfect for standalones, embeds, Codepen-style demos, and most scrollytelling.
2. **Observable Plot** — fast statistical charts when D3's low-level API is overhead (`https://cdn.jsdelivr.net/npm/@observablehq/plot`); keep D3 for scales/data wrangling underneath.
3. **ECharts** (`echarts`) — when you need heavy canned interactivity fast (dashboards, complex linked views) and accept opinionated defaults.
4. **Svelte + D3** — for reactive, multi-component, or state-driven pieces. Common pattern in the dataviz community: Svelte handles DOM updates, state, and layout reactively while D3 does what it's best at (scales, shapes, joins, transitions) — this makes D3 *easier*, not harder. Don't reserve it for "app-like" complexity only; reach for it whenever manual DOM syncing in plain D3 gets tedious.
5. **Tableau/Flourish embeds** — never; code gives control.

Rule of thumb: **the simplest tool that ships.** A build step must buy real value (components, dev speed on a large piece) — otherwise it's friction.

## 🏗️ Plain HTML Boilerplate (memorize this shape)

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Chart title that states the takeaway</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="chart-header">
    <h1>Explanatory headline</h1>
    <p class="subtitle">Context: what, where, when</p>
  </header>
  <main id="chart" aria-label="Short description of the chart for screen readers"></main>
  <footer class="chart-footer">
    <p class="caption">Source: … · Method: … · By …</p>
  </footer>
  <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
  <script src="script.js"></script>
</body>
</html>
```

- Data: fetch a CSV/JSON **next to the file** (`d3.csv("data.csv")`) or inline small data as a `<script type="application/json">` block. For a true single file, inline both data and JS.
- Fonts: `system-ui` stack by default; webfonts (Google Fonts) only when the piece needs brand identity — subset and `font-display: swap`.
- **Never** ship an empty `<div>` chart without `aria-label` / fallback text.

## 🎨 CSS/SCSS

**Plain CSS is fine for single files** — custom properties do the theming:

```css
:root { --ink: #1a1a1a; --muted: #666; --accent: #e63946; --bg: #fff; --grid: #eee; }
```

**SCSS when the project has multiple pieces** (a graphics-desk pattern). Structure:

```
scss/
├── _variables.scss   // colors, fonts, spacing as tokens
├── _base.scss        // reset, typography, .chart-header/.chart-footer
├── _chart.scss       // axes, tooltips, legend primitives (shared)
└── main.scss         // @use everything; page-specific last
```

- Compile with `sass scss/main.scss css/main.css` (Dart Sass, `@use` not `@import`).
- Tokens over literals: never scatter hex codes through component styles.
- Chart CSS belongs in CSS, not inline JS attributes — position/size via CSS; D3 for data-driven marks.

## ⚡ Svelte Setup (the reactive D3 path)

Svelte's role is **reactive glue around D3**, not a replacement: D3 keeps owning scales/shapes/transitions, Svelte owns the DOM skeleton, state, and reactivity. Set up:

```bash
npm create vite@latest my-viz -- --template svelte
npm i -D d3
```

- One component per chart (`src/lib/components/Scatter.svelte`); data loading in a `onMount` or a load function.
- Let **Svelte own the DOM skeleton** (headings, layout, legend) and **D3 own the data-driven marks** (scales, joins, transitions) — render into a `<g>` via an action (`use:d3chart={data}`), not `{#each}` for complex marks.
- Svelte transitions (`transition:`) for enter/exit when simple; D3 `.transition()` for data-driven animation.
- Build to static: `vite build` → deploy `dist/`.

## 📊 The Dataviz Layer (applies to every library)

- **Reuse the dataviz-principles skill's rules**: represent-values vs distinguish-groups, title taxonomy (explanatory default), highlight-and-grey, direct labeling over legends, fixed facet scales, honest axes. The web adds: **tooltips, hover states, transitions, and scroll choreography must reveal insight, not decorate.**
- **Scales & data**: `d3.scale*` with explicit domains; parse dates with `d3.timeParse`, numbers via `d3.autoType`. Never trust CSV types.
- **Responsiveness**: charts re-render on resize via `ResizeObserver` on the container (not `window.resize`), or an SVG with `viewBox` + fluid text sizing. Test at 320px, 768px, 1280px.
- **Tooltips**: position with `getBoundingClientRect`, keep inside viewport, never cover the point, hide on `mouseleave` and `Escape`. Accessible alternative: visible labels where feasible.
- **Transitions**: 250–750ms, ease (`d3.easeCubicOut` default), respect `prefers-reduced-motion: reduce` → snap instantly.

## 🎬 Scrollytelling

**Default pattern — sticky graphic + stepping text:**

```html
<main class="scrolly">
  <figure class="sticky">
    <div id="chart"></div>
  </figure>
  <article class="steps">
    <section data-step="0" data-message="Initial view">…</section>
    <section data-step="1" data-message="Highlight urban areas">…</section>
    <section data-step="2" data-message="Contrast with 2000">…</section>
  </article>
</main>
```

```css
.scrolly { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 4fr); gap: 2rem; }
.sticky { position: sticky; top: 0; height: 100svh; align-self: start; }
.steps section { min-height: 90svh; padding: 1.5rem; background: rgba(255,255,255,.9); }
@media (max-width: 768px) { .scrolly { grid-template-columns: 1fr; } }
```

- **IntersectionObserver over scrollama for simple pieces** (zero deps):

```js
const steps = document.querySelectorAll(".steps section");
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) {
    const message = e.target.dataset.message;
    update(message); // swap highlight, filter, annotation
  }});
}, { rootMargin: "-45% 0px", threshold: 0 });
steps.forEach(s => observer.observe(s));
```

- Use **scrollama** (`https://cdn.jsdelivr.net/npm/scrollama`) when steps need progress-driven **scrubbing** (0–1 progress → e.g. a year scrub).
- Every step changes **exactly one** visual state; steps that change everything at once lose readers. Steps are sentences in a story — each with a subject.
- Mobile: test the sticky pattern on real iOS — `100vh` bugs → use `100svh`.
- Alternative layouts: stacked chapters (chart flows inline with text, sticky only for a map/hero), horizontal scroll panels (careful — breaks reading flow).

## 🌐 Getting It Online

- **GitHub Pages** (zero-cost default): repo → Settings → Pages → deploy from `main` `/root` (or `/docs`). Single-file pieces: just push. Custom domain + HTTPS via the same panel.
- **Netlify/Vercel** when you need preview deploys per branch or Svelte builds: connect repo, build command `npm run build`, publish `dist/`.
- **Embedding elsewhere**: standalone file = `<iframe src="https://…/chart.html" title="…" loading="lazy" style="width:100%;border:0"></iframe>`; size the iframe responsively (aspect-ratio wrapper). PostMessage for iframe↔host height communication; **avoid** `document.write`-era embeds.
- Relative paths everywhere (`./data.csv`), lowercase filenames, no spaces — survives any host.
- Performance budget: first paint < 1s on 4G. Inline critical CSS for single files; full D3 via CDN ~ 280kb gz is acceptable, but for one small chart consider `d3-scale` + `d3-shape` submodules instead.

## ♿ Accessibility & Verification (mandatory before shipping)

1. **Alt text / aria-labels** on every chart container; data tables (`<table>`) as accessible fallback for key figures.
2. **Keyboard**: interactive marks focusable (`tabindex`, `:focus` styles); tooltips also open on focus; no pointer-only interactions for critical info.
3. **Contrast**: labels/annotations ≥ APCA Lc 45 against the chart background (including text over gridded panels).
4. **Colorblind + grayscale check** — same standard as the advanced-ggplot-2 skill; the web adds: hover-only distinctions must also exist statically or via a second cue.
5. **`prefers-reduced-motion`** honored in every transition and scroll animation.
6. **Responsive sweep**: 320 / 768 / 1280px + real mobile touch pass (tap targets ≥ 40px).
7. **No console errors**; fetch failures degrade to a visible error message, not a blank page.
8. **Lighthouse pass** ≥ 90 performance / 100 accessibility for embeds (the host page shares the budget).
9. **Slow data**: never block render on a slow CSV — skeleton or inline the critical data first.
10. **Story check**: a cold reader states the takeaway after ~5 seconds, before any interaction.

## ❌ Never

- Blank chart containers without markup/aria context ("the JS will fill it")
- Hover/click as the *only* way to read a value (tooltip-only labels for key data)
- Fixed pixel widths on charts; un-debounced `window.resize` handlers
- Scrollytelling where the graphic jumps layout at each step (only marks/highlights change)
- Build tooling for a single static chart
- Autoplaying transitions > 1s; parallax + fixed backgrounds + scroll animation combined
- Skipping the reduced-motion check in D3 mutations and IntersectionObserver pieces
