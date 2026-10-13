---
name: |
  web-dataviz
description: |
  Use when building HTML-driven interactive data visualizations — standalone D3/ECharts/Observable Plot charts, embedded graphics, scrollytelling pieces, or expressive web-based art. Covers the full web-dev side including HTML boilerplate, SCSS structure, Svelte setup, responsive/accessibility requirements, and deployment, across audiences and purposes from analytical to expressive.
metadata:
  author: Cédric Scherer
  version: "1.2"
---

# Web Dataviz — HTML-Driven Interactive Visualizations

Act as a **creative web developer + data visualization engineer**. Build standalone, embeddable, and scroll-driven data graphics for the web. Default stack: **plain HTML + modern CSS/SCSS + D3.js, no build step**. Escalate to Svelte when reactivity, shared state, or many components make plain DOM updates painful — Svelte is a thin reactive layer around D3, not a rewrite.

##  Scope & Handoff

This skill covers the **chart/graphic layer** — the visualization itself, its interactivity, and its page as a chart vehicle. When the task is a **complete webpage or app** (portfolio site, multi-page project, custom client web work built with React/Next.js and component libraries like shadcn/ui), load the **web-dev-projects** skill instead — it owns project structure, stack selection, styling conventions, and deployment. Web-dev-projects hands back to this skill for chart internals, so **do not duplicate chart craft there**; and conversely, do not pull Next.js into this skill. One-line rule: *page-first → web-dev-projects; chart-first → stay here.*

##  Stack Selection (in order of preference)

1. **Plain HTML + D3** — the default. One self-contained `.html` file, script via CDN (`https://cdn.jsdelivr.net/npm/d3@7`), zero build. Perfect for standalones, embeds, Codepen-style demos, and most scrollytelling.
2. **Observable Plot** — fast statistical charts when D3's low-level API is overhead (`https://cdn.jsdelivr.net/npm/@observablehq/plot`); keep D3 for scales/data wrangling underneath.
3. **ECharts** (`echarts`) — when you need heavy canned interactivity fast (dashboards, complex linked views) and accept opinionated defaults.
4. **Svelte + D3** — for reactive, multi-component, or state-driven pieces. Common pattern in the dataviz community: Svelte handles DOM updates, state, and layout reactively while D3 does what it's best at (scales, shapes, joins, transitions) — this makes D3 *easier*, not harder. Don't reserve it for "app-like" complexity only; reach for it whenever manual DOM syncing in plain D3 gets tedious.
5. **Tableau/Flourish embeds** — never; code gives control.

Rule of thumb: **the simplest tool that ships.** A build step must buy real value (components, dev speed on a large piece) — otherwise it's friction.

## ️ Plain HTML Boilerplate (memorize this shape)

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

##  CSS/SCSS

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

##  The Dataviz Layer (applies to every library)

- **Reuse the dataviz-principles skill's rules**: represent-values vs distinguish-groups, title taxonomy (explanatory default), highlight-and-grey, direct labeling over legends, fixed facet scales, honest axes, and its style spectrum (analytical ↈݜݛۋY\ڙۙY8dș^ٜܚ]يH8%ؘ]HHYXوڜܝȕH٘ȘYΈ
ʝۛ\ˈݙ\Ȝݘ]\ˈ؛ܚ][ۜˈ[و؜ۛڛܙ[ٜ؜H]\݈ٜݙHHYXى܈[ݙ[݈8%ٝ٘[[ܚYڝ܈[]ٜș[Yڝڙ[ȝHYXو\ș^ٜܚ]ًʊH
ʔؘ[\ȉș]JʎȘ˜ؘ[J؈ڝ^XڝۘZ[܎Ȝ\ܙH]\ȝڝ˝[YT\ܙXݛXٜ܈ژH˘]]՞\Xȓٜٝȝݜ݈ԕȝ\\˂ˈ
ʔٜܛۜڝٜٛ܊ʎȘژ\ݜȜً\ٛٙ\țۈٜڞوژHٜڞٓ؜ٜݙ\؈ۈHۛݘZ[ٜȊ۝ڛٛ݋ܙ\ڞ٘
K܈[ȔՑȝڝڙ]Лޘ
ș۝ZY^ڞڛًȕ\݈]̌͎LΌH
ʕۛ\ʊΈܚ][ۈڝٝ۝[ٚ[ِۚY[ݔ٘ݘٙ\[ܚYHڙ]ܛܝٜٝȘ۝ٜȝHڛ݋YHۈ[ݜٛX]٘[و\ؘ\XȐXؙ\ܚXۙH[\ۘ]]َȝڜژۙHXٛȝڙ\و٘\ژۙKH
ʕ؛ܚ][ۜʊΈ͌8$͍L\ˈX\و
˙X\ِݘژӝ]Y؝[
KٜܙX݈ٜٙ܋\ٙXٙ[[ݚ[ێȜٙX٘8dȜۘ\[ܝ[ݛKȈȼ'㫈؜ۛ][[قʑY؝[]\ۈ8%ݚXڞHܘ\XȊȜݙ\[و^ʊؘ[ϛXZ[Șۘ\܏HܘܛۛHςȈڙݜوۘ\܏HܝXڞHςȈ]ȚYHؚ\݈Ϗٚ]ςȈٚYݜُ\ݚXۙHۘ\܏Hܝ\ȏ٘ݚ[ۈ]K\ݙ\Ḧș]K[Y\ܘYُHқڝX[ڙ]ȏؠ)ϋܙXݚ[ۏ٘ݚ[ۈ]K\ݙ\Ḧș]K[Y\ܘYُHҚYڛYڝ\ؘ[Ș\٘\ȏؠ)ϋܙXݚ[ۏ٘ݚ[ۈ]K\ݙ\Ḧș]K[Y\ܘYُHЛ۝؜݈ڝ̌ϸ)ϋܙXݚ[ۏ؜ݚXۙOۘZ[ςؘܜܘܛۛHș\ܛ^NșܚYșܚY][\]KXۛ[[܎țZ[ۘ^
Y܊HZ[ۘ^
܊Nș؜Ȍܙ[NȟB˜ݚXڞHȜܚ][ێȜݚXڞNȝ܎ȌȚZYڝȌLݚȘ[Yۋ\ٛΈݘ\ݎȟB˜ݙ\Ȝ٘ݚ[ۈțZ[˚ZYڝȎLݚȜY[َȌKٛ͜NȘؘڙܛݛَȜ٘؊͍K͍K͍KΊNȟBЛYYXH
X^]ڙȍ͎
HȋܘܛۛHșܚY][\]KXۛ[[܎ȌY܎ȟHBؘH
ʒ[ݙ\ܙXݚ[ۓ؜ٜݙ\țݙ\Ȝ؜ۛ[XHۜȜڛ\HYXٜʊȊٜۈ\ʎؘ܂؛݈ۜݙ\ȏH؝[Y[݋ܝY\ޔٛXݛܐ[
˜ݙ\Ȝ٘ݚ[ۈʎۛܝ؜ٜݙ\ȏHٝȒ[ݙ\ܙXݚ[ۓ؜ٜݙ\ʙ[ݜڙ\ȏOȞ[ݜڙ\˙ۜјXڊHOȞȚYȊKڜқݙ\ܙXݚ[يHۛܝY\ܘYوHKݘ\ٙ]٘]\ٝۙ\ܘYَ\]JY\ܘYيNȋˈݘ\YڛYڝڛ\ˈ[ۛݘ][ۂȈ_JNKȜۛݓX\ٚ[ΈˍIHˈٜڛۙȌJNݙ\˙ۜјXڊȏOț؜ٜݙ\˛؜ٜݙJʊNH\و
ʜ؜ۛ[XJʈ
΋˘ٛ˚ܙ[]܋ۙ]ۜKܘܛۛ[XX
Hڙ[Ȝݙ\țٙYۙܙ\܋YڝٛȊʜ؜ݘؚ[يʈ
8$̈ۙܙ\܈8dșKًȘHYX\Ȝ؜ݘʋH]ٜވݙ\ژ[ٙ\Ȋʙ^XݛHۙJʈڜݘ[ݘ]NȜݙ\ȝ]ژ[ٙH]ٜޝ[و]ۘوܙH٘Y\܋Ȕݙ\Ș\وٛݙ[ؙ\Ț[ȘHݛܞH8%XXڈڝHݘڙX݋H[ؚ[Nȝ\݈HݚXڞH]\ۈۈ٘[SԈ8%Lژݙ܈8dȝ\وLݚH[\ۘ]]و^[ݝΈݘXڙYژ\\܈
ژ\݈ۛݜȚ[ۚ[وڝ^ݚXڞHۛHۜȘHX\ڙ\ۊKܚ^ۛݘ[؜ۛ[ٛȊ؜ٙݛ8%ܙXZ܈٘Y[وۛ݊KȈȼ'㤈ٝ[و]ۛ[قH
ʑڝXȔYٜʊȊٜۋX݈ۜY؝[
NȜٜȸdȔٝ[ٜȸdȔYٜȸdș\ވܛۈXZ[؈ܛ۝
܈ٛ؜؊KȔڛٛKYڛHYXٜΈݜ݈\ڋȐݜݛۈۘZ[ȊȒȝژHH؛YH[ٛH
ʓٝYދՙ\ؙ[
ʈڙ[Ȟ[݈ٙYٝڙ]ș\ޜȜ\Șܘ[ؚ܈ݙ[Hݚ[ΈۛۙX݈ٜˈݚ[ۛ[X[وܛHݛȘݚ[Xۚ\ڈ\݋؋H
ʑ[Xٙ[و[ٝڙ\يʎȜݘ[٘[ۙHڛHHYܘ[YHܘψڝ΋˸)˘ژ\݋ڝ[ȝ]OHؠ)Ȉؙ[ُHۘ^ވȜݞ[OHݚY̌	N؛ܙ\ΌϏڙܘ[YO؎ȜڞوHYܘ[YHٜܛۜڝٛH
\ܙX݋\؝[ȝܘ\\ʋȔܝY\ܘYوۜȚYܘ[YxeܝZYڝۛ[][ژ؝[ێȊʘ]ۚY
ʈ؝[Y[݋ݜڝXY\؈[Xٙ˂ˈٛ]]و]ș]ٜޝڙ\و
˙]K؜ݘ
Kݙ\ؘ\وڛ[؛Y\ˈۈܘXٜȸ%Hݜݚ]ٜȘ[ވܝH\ٛܛX[ؙHݙٝșڜܝZ[݈\țۈˈ[ۚ[وܚ]X؛ԔșۜȜڛٛHڛ\ΈݛȝژHѓȟȌΌ؈ވ\ȘXؙ\XۙKݝۜțۙHۘ[ژ\݈ۛܚY\Ș˜ؘ[X
Ș˜ژ\Xݘۛٝ[\Ț[ܝXYȈȸƯȐXؙ\ܚXڛ]H	ȕٜڙژ؝[ۈ
X[٘]ܞHٙۜوښ\[يBKȊʐ[^Ș\ژK[Xٛʊțۈ]ٜވژ\݈ۛݘZ[ٜΈ]HXۙ\ȊXۙO؊H\ȘXؙ\ܚXۙH؛ؘڈۜȚٞHڙݜٜˈ[^ۛݜȝH]]ڞ˜ڛؚ\\șۜ۝[NȘژ\݈\H8dș]H\؜ڜ[ۈ8dȚٞH[ܚYڝȘۛ\[Y[݈HڜژۙH؜[ۋۉ݈\X؝H]ˈ
ʒٞXۘ\يʎȚ[ݙ\ؘݚ]وX\ڜșۘݜؘۙH
Xڛٙ^ٛ؝\؈ݞ[\ʎȝۛ\Ș[ۈܙ[țۈۘݜΈۈڛݙ\˛ۛH[ݙ\ؘݚ[ۜșۜȘܚ]X؛[ٛ˂̋Ȋʐۛݜ؜݊ʎțXٛ˘[ۛݘ][ۜȸ©HTЈȍHYؚ[ܝHژ\݈ؘڙܛݛو
[؛Y[و^ݙ\șܚYY[ٛʋȊʐۛܘۚ[و
șܘ^\ؘ[HڙXڊʈ8%؛YHݘ[٘\و\ȝHY؛ؙYYٜ݋LȜښ[ȝH٘ȘYΈݙ\˛ۛH\ݚ[؝[ۜț]\݈[ۈ^\݈ݘ]X؛H܈ژHH٘ۛوݙKKȊʘٜٙ܋\ٙXٙ[[ݚ[ۊʊȚۛܙY[ș]ٜވ؛ܚ][ۈ[و؜ۛ[ڛX][ۋˈ
ʔٜܛۜڝوݙY\
ʎȌ̌ȍ͎ȌLΌ
Ȝ٘[[ؚ[Hݘڈ\܈
\\ٙ]ȸ©H
Kˈ
ʓۈۛܛۙH\ܛܜʊΈٝڈؚ[\ٜșYܘYHȘHڜژۙH\ܛ܈Y\ܘYً۝Hۘ[ڈYًȊʓYڝݜو\܊ʈ8©HL\ٛܛX[ؙHȌLXؙ\ܚXڛ]Hۜș[XٙȊHܝYوژ\ٜȝHݙٝ
KKȊʔ݈ۛ]JʎțٜٝȘؚۛȜٛٙ\țۈH݈ۛԕȸ%Hڙ[]ۈ܈[ۚ[وHܚ]X؛]HڜܝLȊʔݛܞHڙXڊʈ
[؛]X؛[وݜݛۋY\ڙۙYYXٜʎȘHۛ٘Y\Ȝݘ]\ȝHZ٘]؞HYݙ\ȟ͈ٜ٘ۛˈٙۜو[ވ[ݙ\ؘݚ[ۋȑ^ٜܚ]وYXٜȜښ\\ȸ%Hݞ[HܙXݜݛHݛ\șܛۈ]]ڞ˜ڛؚ\\Ș\KȈȸǣٜٝˈۘ[ڈژ\݈ۛݘZ[ٜ܈ڝݝX\ڝ\؜ژHۛݙ^
ݚHԈڛڛ]ʂˈݙ\˘ۚXڈ\ȝH
ۛ۞Jȝ؞HȜ٘YH؛YH
ۛ\[ۛHXٛșۜȚٞH]JBˈڞY^[ڙțۈژ\ݜΈ[˙X۝[ؙYڛٛ݋ܙ\ڞ٘[ٛ\܂ˈ؜ۛ][[وڙ\وHܘ\XȚݛ\ț^[ݝ]XXڈݙ\
ۛHX\ڜ˚YڛYڝȘژ[ٙJBˈݚ[ۛ[وۜȘHڛٛHݘ]XȘژ\݂ˈ]]ܛ^Z[و؛ܚ][ۜȏȌ\Έ\؛^
șڞYؘڙܛݛٜȊȜ؜ۛ[ڛX][ۈۛXڛٙˈښ\[وHٙXٙ[[ݚ[ۈڙXڈ[ȑț]]][ۜȘ[و[ݙ\ܙXݚ[ۓ؜ٜݙ\ȜYXٜ