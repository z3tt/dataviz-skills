---
name: |
  ggplot-2-uncharted-drafter
description: |
  Use when drafting or editing ggplot2 [un]charted lessons or exercises in .tsx files. Load for any task involving course Content.tsx, TopOfPost.tsx, exercises.tsx, or quizzQuestion.tsx files.
---

# ggplot2 [un]charted Course Drafter

Your **only job** is to edit `.tsx` files in the **current lesson directory** to match the style, tone, and structure of the course's reference lessons:

- `app/module1/aesthetics/TopOfPost.tsx` + `Content.tsx`
- `app/module3/styling-text/TopOfPost.tsx` + `Content.tsx`

**NEVER** modify reference files or files outside the current directory.

## 📌 Core Rules (Non-Negotiable)

### 1. Lesson Anatomy

Every lesson folder contains:
- `TopOfPost.tsx` — the hook above the fold: one big question or claim (`<h2>🗺️ A World of …</h2>`), 1–3 short paragraphs, often a teaser component or sandbox, no exercises.
- `Content.tsx` — main body with `"use client";`, imports, `export const Content = () => (…)`.
- `exercises.tsx` — exercise definitions consumed by `ExerciseAccordion` / `ExerciseDoubleSandbox` in `Content.tsx` (ids like `"M1-L2-principles-first-plot"`).
- `quizzQuestion.tsx` (optional) — quiz data for `MultipleQuizzWrapper`.

Recurring **Content section flow** (adapt, don't force):
1. Hook / problem — often a deliberately broken or surprising chart
2. "Okay, so what's going on?" — explain the mechanism
3. ✅ The Fix — corrected code, tabbed (`Tabs`/`TabsList`) variants
4. 🪄 The general rule — bolded key principle
5. Interactive exploration — side-by-side code comparisons
6. `<h2>🏆 Exercises</h2>` via `ExerciseAccordion`
7. Optional: 📋 Recap / 🚀 What next?

### 2. Style & Tone

- **Voice**: Light, playful, second person, code-first. Explain jargon in one sentence. Meta-jokes allowed ("Doesn't that sound great? 😄").
- **Paragraphs**: 1–3 sentences max. No walls of text. No filler ("In this section, we'll…" → "Let's…"). No summaries/teasers between sections.
- **Headings** (`<h2>`, `<h3>`): start with **one emoji**, title case, max ~7 words (e.g., `🧱 Building Plots Like Sentences`, `🪤 Palette Pitfalls`, `🐇 Going Down the Rabbit Hole` for optional depth).
- **Sidenotes**: witty, max 2 sentences, often self-aware ("Yes, we might be biased but…"). Use `<details>` collapses for "No idea? Here's the explanation 🤗".

### 3. Highlight Semantics (strict)

| Class | Meaning |
|---|---|
| `simple-highlight-gold` | key principle / takeaway |
| `simple-highlight-teal` | secondary emphasis, new terms |
| `simple-highlight-red` | warnings, critical distinctions |
| `simple-highlight-orange` | caveats |
| `simple-highlight-purple` / `-blue` | occasional special terms |
| `simple-highlight-black` / `-white` | code-like/neutral emphasis |

Wrap highlighted words with `&nbsp;`/`&ensp;` padding inside the span.

**Course color set** (from the SCSS; use these — never other colors — when lessons need inline colors):
- **Set 1 (dark variants):** red `#d13760`, orange `#e75f00`, gold `#c69612`, teal `#00978a`, blue `#006d93`, purple `#663e8e`
- **Set 2 (light variants, used as highlight backgrounds):** red `#ff8da3`, orange `#ffa693`, gold `#f8c663`, teal `#88ebdd`, blue `#a0d5ff`, purple `#d8bbff`
- Highlight classes pull from Set 2 (`simple-highlight-purple`/`-black` force `color: #000`); Tailwind grays (`--color-gray-*`) for neutral chrome.

### 4. Components

Use only the course component vocabulary (reuse patterns from references):
`Sidenote` · `ResponsiveREditor` (from `@/components/REditor`) · `ExerciseAccordion` · `DidYouKnowCard` · `ExerciseDoubleSandbox` · `CodeBlock` · `DatasetPreviewButton` · `Tabs`/`TabsList`/`TabsTrigger`/`TabsContent` (from `@/components/ui/tabs`) · `MultipleQuizzWrapper`/`MultipleChoice` · `RPlotWithSandbox` · `Caption` · `Confetti` · `BeforeAfterSlider` · `Spacing`.

**Never** introduce new components unless explicitly requested.

### 5. R Code Conventions (in sandboxes)

- `library(ggplot2)` at the top of every snippet.
- **Mixed style as course standard**: `ggplot(mpg, aes(displ, hwy))` — clean, saves typing `data =`/`mapping =`.
- `.trim()` on every `initialRCode={…}` template literal.
- Comments mark intent (`# all arguments are named`, `# no arguments are named`).
- Course datasets via URL: `read.csv("https://www.ggplot2-uncharted.com/data/<name>.csv")`.

### 6. Datasets

**Preferred order**:
1. Course datasets: Palmer penguins (course version), `Gapminder`, `HYDE`, Simpsons ratings
2. R datasets: `mpg`, `airquality`, `msleep`
3. Other course datasets (check `public/data/data-description.tsx` if unsure)

When introducing a dataset: use `DatasetPreviewButton` and briefly remind readers of its purpose.

### 7. Exercises

Separate `exercises.tsx` with `toDo`, `whyItMatters`, `practiceSandbox`, `solutionSandbox`:
- **toDo**: real-world scenario ("Your boss asked you to…") or follow-up task; numbered steps if >2 actions; hints/links to lesson content, **no full code** in early exercises.
- **whyItMatters**: broader data-communication context (audience, message, comparison).
- **practiceSandbox**: starter snippet, no task-listing comments.
- **solutionSandbox**: full solution with brief explanatory comments.

### 8. File Editing

- Directly edit files in the current lesson directory (no diff proposals unless asked).
- Minimal, focused edits. Preserve imports, exports, route metadata, layout wrappers.
- Ask before creating new files.
- Custom-font demos get an install-hint box (see **Fonts** below).

### 9. Fonts (course-specific — not the user's personal style)

The course uses fixed fonts in its R code examples — follow them when lessons render text or demonstrate custom typography:

- **Rethink Sans** — base text (axis labels, subtitles, body-like plot text)
- **Domine** — plot titles
- Loaded via `showtext`/`sysfonts` in lesson sandboxes (`font_add(...)`, `theme(..., family = ...)`).

Any lesson that renders custom fonts gets an install-hint box before the first such snippet:

```tsx
<SideNote emoji="🛠️" title="Before You Run the Next Codes">
  …install Rethink Sans + Domine…
</SideNote>
```

These are *course* fonts tied to the course's visual identity — do not swap them for other or personal typefaces.

## ✅ Do This (Example Section)

```tsx
<h2>🎨 Color It Your Way</h2>
<p>
  Depending on the variable you map to <code>color</code>,{" "}
  <code>ggplot2</code> picks a categorical palette or a continuous gradient.
</p>
<div className="full-bleed my-3">
  <Tabs defaultValue="a" className="relative mt-5">
    …
  </Tabs>
</div>
<div className="relative">
  <Sidenote
    text={
      <span>
        <em>"Wait, data what…?"</em> 🤯 <br />
        No worries, our bonus lesson{" "}
        <a href="/bonus/intro-to-r">Quick Intro to R</a> has you covered.
      </span>
    }
  />
  <p>As you can see, <b>the data type drives the default</b>.</p>
</div>
```

## ❌ Never Do This

| Violation | Bad | Fix |
|---|---|---|
| Long paragraphs | "In this section, we will explore…" | "Let's explore…" |
| Missing emoji in headings | "Color it Your Way" | "🎨 Color it Your Way" |
| New components | `<CustomWidget>` | Use allowed components only |
| Formal language | "Utilize `facet_wrap()`" | "Use `facet_wrap()`" |
| Full code in early exercises | Complete solution in `toDo` | Hints, not solutions |
| Modifying reference files | Editing `module1/aesthetics/…` | Only edit current lesson |
| Ignoring dataset preferences | Using `mtcars` | Use `mpg` or penguins |

## 🔍 Reference Phase (Always Do This First)

1. **Read** the 4 reference files (TopOfPost + Content for `module1/aesthetics` and `module3/styling-text`).
2. **Adopt** their heading hierarchy, paragraph length, tone, component patterns, highlight semantics, and section flow.
3. **Open** the target file(s) in the current lesson directory. Empty → create from reference patterns (after confirmation). Existing → align to reference style.
4. **Never** scan unrelated directories unless explicitly requested.
