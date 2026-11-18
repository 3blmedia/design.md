---
version: alpha
name: 3BL-common-brand
description: "3BL brand system from the 2026 Brand Guidelines (Type + Color). IBM Plex Sans for UI and body. IBM Plex Serif for editorial headlines. Ink #181E28, wash #F1F1F0, primary #3687FF, mist #98BCCD, sage #93BEB5. Marketing, UX/UI, and product palettes are separate tiers."

colors:
  ink: "#181E28"
  wash: "#F1F1F0"
  primary: "#3687FF"
  on-primary: "#FFFFFF"
  mist: "#98BCCD"
  sage: "#93BEB5"
  slate: "#43576B"
  slate-muted: "#9DAABD"
  focus-deep: "#0F2829"
  focus-green: "#2B6A3F"
  compass-violet: "#2E283C"
  compass-cream: "#EAE2CF"
  studio-lime: "#A3FF6C"
  studio-stone: "#96A09C"
  studio-purple: "#685C84"
  studio-lilac: "#9F9DA9"
  studio-peach: "#F7B6A0"
  studio-taupe: "#A6A094"
  white: "#FFFFFF"
  black: "#000000"

typography:
  display:
    fontFamily: IBM Plex Sans
    fontWeight: 300
    notes: "Hero display. Tight negative tracking on marketing."
  headline-serif:
    fontFamily: IBM Plex Serif
    fontWeight: 500
    notes: "Section headlines"
  headline-serif-strong:
    fontFamily: IBM Plex Serif
    fontWeight: 600
    notes: "Article titles"
  body:
    fontFamily: IBM Plex Sans
    fontWeight: 400
  body-light:
    fontFamily: IBM Plex Sans
    fontWeight: 300
    notes: "Large reading blocks"

rounded:
  sm: 8px
  md: 12px
  pill: 22px

spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  section: 64px
---

# Design system: 3BL common brand

> Source: 3BL 2026 Brand Guidelines, Type + Color (internal PDF).
> Product DESIGN.md files inherit this file unless they override a token.

## 1. Visual theme and atmosphere

Navy ink, cool wash backgrounds, one blue accent (`#3687FF`). IBM Plex Sans for product and UI. IBM Plex Serif for editorial headlines. Flat surfaces. Color roles split into Marketing, UX/UI, and Product. Do not invent extra hues.

**Inherits:** none. This is the root brand file.

## 2. Color palette and roles

### Marketing
| Role | Hex | Use |
|------|-----|-----|
| Ink | `#181E28` | Primary text, dark bands, wordmark |
| Wash | `#F1F1F0` | Light page background |
| Primary accent | `#3687FF` | CTAs, links, highlights |
| Mist | `#98BCCD` | Secondary accent, charts, links on dark |
| Sage | `#93BEB5` | Supporting accent |

### UX / UI
| Role | Hex | Use |
|------|-----|-----|
| Ink | `#181E28` | Titles, primary text |
| Slate | `#43576B` | Secondary text, icons |
| Slate muted | `#9DAABD` | Tertiary, meta |
| Wash | `#F1F1F0` | App backgrounds, panels |
| Primary | `#3687FF` | Interactive accent |

### Products (Focus / Compass / Studio)
| Hex | Notes |
|-----|-------|
| `#0F2829`, `#2B6A3F` | Focus greens |
| `#2E283C`, `#EAE2CF` | Compass violet and cream |
| `#A3FF6C`, `#96A09C`, `#685C84`, `#9F9DA9`, `#F7B6A0`, `#A6A094` | Studio set |
| `#FFFFFF`, `#000000` | White, black |

**Rule:** Marketing for public marketing sites. UX/UI for portals and tools. Product accents only inside product-branded modules.

## 3. Typography rules

| Role | Family | Weight |
|------|--------|--------|
| Display / hero | IBM Plex Sans | 300 |
| UI / nav / body | IBM Plex Sans | 400 |
| Section headlines | IBM Plex Serif | 500 |
| Strong titles | IBM Plex Serif | 600 |

Get Plex Sans and Plex Serif from Google Fonts or Adobe Fonts per the guidelines.

## 4. Component stylings

- Primary CTA: `#3687FF` fill with white label, or ink/white outline pills at about 22px radius.
- Links: `#3687FF` on marketing and UI. Mist `#98BCCD` on dark editorial.
- Surfaces: wash or white on light pages. Ink or navy bands for contrast sections.
- Do not invent purple gradients or terracotta accents.

## 5. Layout principles

Wide section spacing. Hierarchy is eyebrow, then headline, then body. One accent color per composition. Use full-bleed photography or product UI as the main image, not abstract decoration.

## 6. Depth and elevation

Flat surfaces and hairline dividers. Soft shadows only in admin or portal UI. See the Gin portal DESIGN.md. Marketing separates sections with color bands, not stacked shadows.

## 7. Do's and don'ts

**Do**
- Use IBM Plex on brand-owned surfaces unless a product DESIGN.md documents an exception.
- Keep `#3687FF` as the primary interactive accent.
- Pick Marketing, UX/UI, or Product colors by context.

**Don't**
- Mix product accent sets into marketing heroes without a product reason.
- Replace Plex with Inter, Roboto, or system stacks on branded marketing pages.
- Stack many competing accent hues on one page.

## 8. Responsive behavior

Use clamp-style fluid type on marketing sites. Keep AA contrast for ink on wash and white on ink. Touch targets at least 44px.

## 9. Agent prompt guide

- "Use 3BL common brand: IBM Plex Sans/Serif, ink `#181E28`, wash `#F1F1F0`, accent `#3687FF`."
- "Marketing page: wash canvas, navy ink type, pill CTAs, one blue accent."
- "UX surface: slate `#43576B` / `#9DAABD` for secondary text. Blue for actions only."
- "Stay within Brand Guidelines 2026. No purple theme."
