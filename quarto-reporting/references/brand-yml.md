# brand.yml Field Reference

Reference for `_brand.yml` — the machine-readable brand specification auto-discovered by Quarto (and usable in Shiny via bslib). Load when creating or modifying brand files.

## Structure

```yaml
color:
  palette:            # named colors, referenced elsewhere
    brand-blue: "#0066cc"
  primary: brand-blue  # semantic assignment (reference, not hex)
  secondary: brand-gray
  success: ...
  warning: ...
  danger: ...
  foreground: "#333333"
  background: "#ffffff"

typography:
  fonts:               # font definitions, before use
    - family: Inter
      source: google   # google | file | kit
      weight: [400, 600, 700]
      style: [normal, italic]
      # file: fonts/Inter-Variable.woff2   (when source: file)
  base:
    family: Inter
    size: 16px
    line-height: 1.5
  headings:
    family: Inter
    weight: 600
  monospace: Fira Code

logo:
  small: logos/icon.png
  medium: logos/header.png
  large: logos/full.svg
  # light/dark variants for themed outputs

meta:
  name: Company Name
  link: https://example.com
```

## Rules

- All fields optional — include only what's needed.
- Hex colors quoted: `"#0066cc"`.
- Lowercase hyphenated names: `brand-blue`, `success-green`.
- Define palette entries and fonts **before** referencing them.
- URLs include `https://`.
- For color shades/tints ranges, pick the midpoint color.
- Semantic slots (`primary`, `success`, `warning`, `danger`) map components automatically.

## Light/Dark Variants

Outputs supporting them can carry both:

```yaml
color:
  palette:
    ink: "#1a1a1a"
    paper: "#ffffff"
  primary: brand-green
  background: paper
  foreground: ink
  light:
    background: paper
    foreground: ink
  dark:
    background: "#121212"
    foreground: "#f0f0f0"
```

## Licensed Fonts (e.g., bought from foundries)

- `source: file` with the font files in the project — never hotlink licensed fonts.
- Check the license's embedding terms before PDF export (print embedding vs. editable vs. installable).
- Subset large variable fonts for web outputs; `font-display: swap` via CSS where applicable.

## Modification Workflow

1. Read the current `_brand.yml` first.
2. Extend the palette — never break existing references (other files may reference names).
3. Update semantic slots rather than hard-coding hex values downstream.
4. Re-render and verify the brand consistency sweep.
