---
version: alpha
name: 3BL-client-portal-gin
description: "Client portal uses default Drupal Gin. Layers #fff / #edeff5 / #eeeff3, ink #222330, secondary text #545560, focus blue rgb(0,125,250), Ginter/Inter UI fonts, soft shadows, control radii about 0.5rem. Brand accent #3687FF may tint primary actions when customized. Baseline is stock Gin."

colors:
  title: "#222330"
  text: "#222330"
  text-light: "#545560"
  disabled: "#767676"
  disabled-bg: "#eaeaea"
  focus: "rgb(0, 125, 250)"
  focus-ring: "rgb(0, 125, 250, 0.6)"
  danger: "#cc3d3d"
  warning: "#d8b234"
  success: "#058260"
  success-text: "#1d6844"
  bg-layer: "#ffffff"
  bg-layer2: "#edeff5"
  bg-layer4: "#e2e5ec"
  bg-header: "#eeeff3"
  bg-input: "#ffffff"
  border: "#d4d4d8"
  border-form: "#8e929c"
  icon: "#414247"
  brand-primary: "#3687FF"

typography:
  font-family: "ginter, inter, Helvetica Neue, blinkmacsystemfont, -apple-system, Segoe UI, roboto, sans-serif"
  size-xxs: 0.75rem
  size-s: 0.875rem
  size-m: 1rem
  size-l: 1.125rem
  size-xl: 1.25rem
  size-h3: 1.5rem
  size-h2: 1.75rem
  size-h1: 1.6rem
  weight-normal: 400
  weight-semibold: 525
  weight-bold: 575

rounded:
  s: 0.375rem
  m: 0.5rem
  l: 0.75rem

spacing:
  xs: "var(--gin-spacing-xs)"
  s: "var(--gin-spacing-s)"
  m: "var(--gin-spacing-m)"
  l: "var(--gin-spacing-l)"
  xl: "var(--gin-spacing-xl)"
---

# Design system: Client portal (Drupal Gin default)

> Source: Drupal Gin theme CSS variables (`--gin-*`), default admin template.
> Inherits brand meaning from [`../common/DESIGN.md`](../common/DESIGN.md) only where customized. Visual UI is Gin, not the marketing site.

## 1. Visual theme and atmosphere

Dense admin UI. Light gray header strip, white content panels, blue focus rings, limited status colors. Matches Drupal Gin defaults. Toolbar and sticky actions. Content sits in white panels on gray `#edeff5`. Not a marketing layout.

## 2. Color palette and roles

| Token | Value | Role |
|-------|-------|------|
| `--gin-color-title` / text | `#222330` | Titles and body |
| `--gin-color-text-light` | `#545560` | Secondary, help |
| `--gin-color-focus` | `rgb(0, 125, 250)` | Focus rings, primary interactive |
| `--gin-bg-layer` | `#fff` | Cards, content |
| `--gin-bg-layer2` | `#edeff5` | Page background |
| `--gin-bg-header` | `#eeeff3` | Top bar |
| `--gin-border-color` | `#d4d4d8` | Dividers |
| `--gin-border-color-form-element` | `#8e929c` | Inputs |
| Status success / warning / danger | `#058260` / `#d8b234` / `#cc3d3d` | Messages |

Optional: map primary buttons to `#3687FF` to match 3BL marketing. Keep Gin neutrals for structure.

## 3. Typography rules

Gin stack: Ginter, Inter, then system UI fonts. Sizes from `--gin-font-size-*`, about 0.75rem to 1.75rem for H2. Weights: 400, about 525 semibold, about 575 bold. Do not force IBM Plex into admin UI unless a brand change is documented.

## 4. Component stylings

- Buttons: primary uses focus blue. Secondary is ghost or border on white. Disabled is `#767676` on `#eaeaea`.
- Inputs: white fill, `#8e929c` border, focus ring from `--gin-color-focus` at about 0.6 alpha.
- Tables: hairline row borders via `--gin-border-color-table`. Stronger header border.
- Messages: tinted status backgrounds (`--gin-status-*-bg`) with matching text tokens.
- Toolbar: about 66px collapsed, 256px expanded. Sticky height about 60px.

## 5. Layout principles

Admin shell: vertical toolbar, sticky top bar, main content column. Spacing from `--gin-spacing-*`. Labels stack above fields. Two-column layouts only when Gin provides them. No marketing full-bleed heroes inside the portal.

## 6. Depth and elevation

```
--gin-shadow-l1: 0 1px 2px rgb(20 45 82 / 0.02), 0 3px 4px rgb(20 45 82 / 0.03), 0 5px 8px rgb(20 45 82 / 0.04)
--gin-shadow-l2: ... + 0 20px 24px rgb(20 45 82 / 0.12)
```

Use L1 for cards and dropdowns. Use L2 for modals and overlays. Transition: `0.15s cubic-bezier(0.19, 1, 0.22, 1)`.

## 7. Do's and don'ts

**Do**
- Stay on Gin tokens for structure, focus, and status.
- Keep focus rings and form label patterns visible.
- Keep content panels white on `#edeff5`.

**Don't**
- Restyle the portal like 3bl.com marketing. No 96px light heroes. No pill outline CTAs as the default.
- Replace Gin focus blue with decorative gradients.
- Drop borders in favor of heavy drop shadows everywhere.

## 8. Responsive behavior

Toolbar collapses. Sticky header stays. Tables scroll horizontally instead of crushing columns. Keep Gin spacing so controls stay tappable.

## 9. Agent prompt guide

- "Client portal UI uses default Drupal Gin: white layers on `#edeff5`, text `#222330`, focus blue, Inter/Ginter stack."
- "Primary actions: Gin focus blue, or `#3687FF` if brand-aligned."
- "No marketing hero patterns inside admin UI."
- "Status colors: success `#058260`, warning `#d8b234`, danger `#cc3d3d`."
