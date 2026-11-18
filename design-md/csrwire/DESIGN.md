---
version: alpha
name: 3BL-csrwire-reportalert
description: "Shared editorial docs for CSRwire (dark) and ReportAlert (light). CSRwire: #0B0F16, mist link #98BCCD, text #F1F1F0 / #d6d6d6, IBM Plex Sans light and Serif body, rounded photo cards. ReportAlert: light page, Proxima Nova UI, slate #242C3A / #485F83, hover #00ADEE, IBM Plex Serif for reading. Same card structure, opposite light and dark values."

colors:
  csr-stage: "#0B0F16"
  csr-panel: "#1e2531"
  csr-text: "#d6d6d6"
  csr-wash: "#F1F1F0"
  csr-link: "#98BCCD"
  csr-hover: "#F1F1F0"
  csr-footer: "#0B0F16"
  ra-ink: "#404040"
  ra-nav: "#242C3A"
  ra-blue: "#485F83"
  ra-hover: "#00ADEE"
  ra-canvas: "#FFFFFF"
  mist: "#98BCCD"
  wash: "#F1F1F0"
  economy: "#AAFBAB"

typography:
  csr-sans:
    fontFamily: ibm-plex-sans, sans-serif
  csr-serif:
    fontFamily: ibm-plex-serif, Georgia, serif
  csr-title:
    fontFamily: ibm-plex-sans, sans-serif
    fontWeight: 200
    fontSize: 35.2px
    letterSpacing: 1px
  ra-sans:
    fontFamily: proxima-nova, sans-serif
  ra-serif:
    fontFamily: ibm-plex-serif, Georgia, serif
  ra-title:
    fontFamily: proxima-nova, sans-serif
    fontWeight: 200
    fontSize: 36px

rounded:
  media-card: 12px
---

# Design system: CSRwire and ReportAlert

> Live capture: https://csrwire.com and https://reportalert.com. ReportAlert is reportalert.com (singular). reportalerts.com does not resolve.
> Inherits: [`../common/DESIGN.md`](../common/DESIGN.md)
> One DESIGN.md for both sites. Shared editorial structure with a dark and a light variant.

## 1. Visual theme and atmosphere

Both sites are 3BL Network editorial destinations with large feature cards (image plus story meta), category chips, and Part of 3BL footer branding.

- **CSRwire.** Near-black canvas `#0B0F16`, mist-blue links `#98BCCD`, light gray body text, Plex Sans 200 to 300 for titles, Plex Serif for body (`--font-body`). Rounded image cards on dark panels.
- **ReportAlert.** Light page, Proxima Nova for UI and titles (weight about 200), Plex Serif for long reading, slate navy wordmark `#242C3A`, cyan hover `#00ADEE`.

Pick one variant explicitly. Do not average them into a mid-gray theme.

## 2. Color palette and roles

### CSRwire
| Token | Hex | Role |
|-------|-----|------|
| `--bg-dark` | `#0B0F16` | Page and footer |
| `--blue-dark` | `#1e2531` | Panels |
| `--text` | `#d6d6d6` | Body text |
| `--link` | `#98BCCD` | Nav and links |
| `--hover` / wash | `#F1F1F0` | Hover and bright text |
| `--economy-color` | `#AAFBAB` | Sparse accent |

### ReportAlert
| Token | Hex | Role |
|-------|-----|------|
| Canvas | white | Page |
| `--blue-dark` | `#242C3A` | Wordmark and nav ink |
| `--blue` | `#485F83` | Secondary blue |
| `--hover` | `#00ADEE` | Interactive hover |
| Body ink | `#404040` | Default text |

## 3. Typography rules

| Site | UI / titles | Body |
|------|-------------|------|
| CSRwire | IBM Plex Sans (200 to 400) | IBM Plex Serif |
| ReportAlert | Proxima Nova (200 to 400) | IBM Plex Serif |

Site title on both: about 35px, weight 200, letter-spacing about 1px. Hero story titles about 35 to 37px. CSRwire nav labels about 13px / 600 in mist.

## 4. Component stylings

**Feature / story cards**
- Large media with about 12px rounded corners.
- Category label above title. Company and date meta in muted type.
- CSRwire: dark text panel beside or under the image. Mist category.
- ReportAlert: light panels. Slate titles.

**Navigation**
- Minimal top nav: Latest, About, Subscribe or Search.
- CSRwire links `#98BCCD`. ReportAlert links `#242C3A`.

**CTA / More**
- Low-emphasis text or a small filled control. Not 3bl.com marketing pills.

**Footer**
- CSRwire: `#0B0F16` with social, legal, and Part of 3BL.
- ReportAlert: light or branded footer with the Network lockup.

## 5. Layout principles

Hero feature, then featured grid (often three columns), then more stories. Editorial density over marketing whitespace. Photography is the main visual. Titles stay light weight.

## 6. Depth and elevation

Flat dark or light backgrounds. Cards separate by fill color and radius, not heavy shadows. Cookie banners may add temporary elevated white panels. Ignore those for brand core.

## 7. Do's and don'ts

**Do**
- Keep CSRwire dark with mist links. Keep ReportAlert light with Proxima and cyan hover.
- Use Plex Serif for long-form on both.
- Keep rounded photo cards and category-before-title order.

**Don't**
- Apply the 3bl.com off-white `#F6FAFF` hero marketing pattern here.
- Swap CSRwire to Proxima or ReportAlert to all-Plex without a redesign brief.
- Use primary `#3687FF` fills as the default CTA. Mist, slate, and cyan are the O&O accents.

## 8. Responsive behavior

Feature split stacks image over text. Three-column grids collapse to one or two columns. Keep Serif body near 60 to 75 characters per line.

## 9. Agent prompt guide

- "CSRwire page: `#0B0F16` canvas, text `#d6d6d6`, links `#98BCCD`, Plex Sans light titles and Plex Serif body, 12px rounded media cards."
- "ReportAlert page: light canvas, Proxima Nova titles weight 200, nav `#242C3A`, hover `#00ADEE`, Plex Serif body."
- "Shared: category, then headline, then company/date meta. Part of 3BL footer."
- "URL: reportalert.com (singular)."
