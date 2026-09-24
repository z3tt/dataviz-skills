---
name: |
  dataviz-workflow
description: |
  Use when starting a new dataviz piece or project — setting up the working directory, tracking decisions and progress, or writing the brief before building. Covers three setup modes depending on the type of work: a change-tracking notepad (any skill), a project directory scaffold (reports, workshops, web dev, plotting projects), and a goals-and-steps brief (technical builds, chart-design decisions, workshop flows, scrollytelling narratives). Provider-agnostic: plain markdown, no tool lock-in.
---

# Dataviz Workflow — Project Setup & Tracking

Set up persistent working structure at the start of a piece, and keep it current. The chat is not the record — the files are. This skill composes with the sibling skills; pick the mode(s) the work needs.

## Mode 1: Tracking notepad (always, any skill)

A single markdown file recording what was decided and done — survives session resets and workspace wipes.

**Location**: in the project dir if one exists (Mode 2); otherwise a `_notes/` dir (ask the user where, if unclear). One file per piece.

**Naming**: `YYYY-MM-DD_kebab-slug.md`

**Shape**:

```markdown
---
status: pending   # pending | in progress | review | blocked | done
piece: <client/project + piece name>
spectrum: analytical | custom-designed | expressive
---

# <Piece title>

## Goal
One sentence: the takeaway the reader should get (per dataviz-principles).

## Work Items
- [ ] First step
- [ ] …

## Decisions & Changes
<!-- every design choice with its reason -->
- 2026-09-24 · palette: corporate mains, green as highlight (message = growth)
- 2026-09-24 · ordering: months kept intrinsic (seasonal cycle matters)
```

Update after every decision, data problem, review round, or export — not only at the end. When in doubt, write it down.

## Mode 2: Project directory scaffold (technical work)

For multi-file pieces: reports, workshops, web dev, (gg)plotting projects.

```
project/
├── NOTES.md            # Mode 1 notepad
├── data/               # raw + processed, never overwrite raw
├── output/             # exports at final size/dpi
├── src/ or R/          # code
└── docs/ or scss/      # per stack (see below)
```

Stack specifics:
- **Reporting/Quarto** → `_brand.yml`, `_quarto.yml`, `report.qmd` (per quarto-reporting)
- **Web dev** → `index.html`, `scss/` token structure (per web-dataviz)
- **Workshop** → `slides/`, `exercises/`, `solutions/`
- **(gg)plotting project** → theme files + palette definitions as reusable objects, kept with the data

## Mode 3: Brief before building (goal & steps)

Written *before* the work starts; the plan the notepad then tracks. Split by type:

**Technical (web dev, reporting, plotting project):**
```markdown
## Brief — <piece>
1. Goal & takeaway (one sentence each)
2. Audience & medium (print/screen/talk/poster)
3. Spectrum position + why
4. Data: source, access, caveats
5. Build steps, ordered, with definition of done per step
6. Verification plan (which checks apply, per sibling skill)
```

**Theoretical (chart discussion, workshop flow, scrollytelling narrative):**
```markdown
## Brief — <piece>
1. Core message & intended feeling
2. Audience assumptions & prior knowledge
3. Decision/question list (charts to discuss, flows to design, steps to choreograph)
4. Structure: sections/steps as a sequence, each with its own sub-message
5. Open questions to resolve with the user
```

Scrollytelling specifics: each step changes exactly one visual state (per web-dataviz) — the brief should list the steps as sentences *before* any code.

## Lifecycle

1. **Start**: ask (or infer) the type of work → create notepad; scaffold dir and/or brief as needed.
2. **During**: keep the notepad current (status, work items, decisions with reasons). Design decisions with rationale are the most valuable content — they justify choices when the work resumes or is reviewed.
3. **Handover/resume**: the notepad is the entry point — a new session reads it first and continues without re-deriving context.
4. **Done**: set `status: done`, ensure final outputs and their locations are recorded.

## Rules

- Never let files replace the sibling skills: chart decisions still follow dataviz-principles; code standards still follow the tool skill. This skill tracks the work; they decide it.
- The brief is a plan, not a contract — revisit when the data says otherwise; record *why* it changed.
- For one-off quick charts, Mode 1 alone is enough — don't scaffold a directory for a single plot (no overkill).
