---
version: alpha
name: 3BL-corp-website
description: "3bl.com marketing site. Canvas #F6FAFF, ink #182334, primary #3687FF, IBM Plex Sans and Serif. Dark hero and product bands, light display headlines, pill CTAs at 22 to 30px radius, dashboard mockups as the main visual. Sections alternate dark and light."

colors:
  canvas: "#F6FAFF"
  ink: "#182334"
  primary: "#3687FF"
  primary-light: "#7DB7FE"
  on-primary: "#FFFFFF"
  white: "#FFFFFF"
  black: "#000000"
  economy: "#AAFBAB"
  hover: "#3687FF"
  link: "#2A5ADB"
  cookie-slate: "#425B76"

typography:
  hero:
    fontFamily: ibm-plex-sans, sans-serif
    fontSize: "clamp(48px, calc(5.65px + 8.82vw), 96px)"
    fontWeight: 300
    letterSpacing: "-2px"
    lineHeight: 0.9
  h1:
    fontFamily: ibm-plex-sans, sans-serif
    fontSize: "clamp(40px, calc(20.59px + 4.04vw), 62px)"
    fontWeight: 300
  h2:
    fontFamily: ibm-plex-serif, Georgia, serif
    fontSize: "clamp(30px, calc(17.65px + 2.57vw), 44px)"
    fontWeight: 500
  h3:
    fontFamily: ibm-plex-sans, sans-serif
    fontSize: "clamp(22px, calc(14.94px + 1.47vw), 30px)"
    fontWeight: 500
  eyebrow:
    fontFamily: ibm-plex-sans, sans-serif
    fontSize: 13px
    fontWeight: 600
    textTransform: uppercase
  body:
    fontFamily: ibm-plex-sans, sans-serif
    fontSize: "clamp(16px, calc(13.35px + 0.55vw), 19px)"
    fontWeight: 400
    lineHeight: 1.5
  button:
    fontFamily: ibm-plex-sans, sans-serif
    fontSize: 15px
    fontWeight: 600

rounded:
  pill: 22px
  pill-lg: 30px

spacing:
  section: 96px
---

# Design system: 3BL corporate website (3bl.com)

> Live capture: https://3bl.com (agent-browser).
> Inherits: [`../common/DESIGN.md`](../common/DESIGN.md)

## 1. Visual theme and atmosphere

Off-white page background `#F6FAFF` with full-width dark navy hero and product bands. Display type is IBM Plex Sans 300 with letter-spacing about -2px. Section stories use IBM Plex Serif 500. Product proof uses dark dashboard mockups, gauges, bars, and radar charts. Outline pill CTAs. Sections alternate dark, light, dark, light.

## 2. Color palette and roles

| Token | Hex | Role |
|-------|-----|------|
| `--off-white` / canvas | `#F6FAFF` | Page background |
| `--blue-dark` / ink | `#182334` | Text on light, dark section fills, outline CTAs |
| `--blue-med` / primary | `#3687FF` | Brand accent, hover |
| `--blue-light` | `#7DB7FE` | Soft highlight, chart secondary |
| White | `#FFFFFF` | Text on dark, login pill fill |
| Link | `#2A5ADB` | Inline links |
| Economy accent | `#AAFBAB` | Sparse positive data highlight |

CSS vars on the live site include `--font-sans`, `--font-serif`, `--fs-hero` through `--fs-caption`, and `--hover: var(--blue-med)`.

## 3. Typography rules

| Level | Spec |
|-------|------|
| Hero H1 | Plex Sans 300, up to 96px, letter-spacing -2px, line-height about 0.9 |
| H2 (story) | Plex Serif 500, about 30 to 44px fluid |
| H3 | Plex Sans 500, about 22 to 30px |
| Eyebrow (H5) | Plex Sans about 13px, uppercase (WHO WE ARE, OUR PRODUCTS) |
| Body | Plex Sans 16 to 19px fluid |
| Button | Plex Sans 15 to 16px / 600 |

Also loads ibm-plex-sans-condensed in a few places. Skip Lato except in third-party cookie UI.

## 4. Component stylings

**Buttons / CTAs**
- Primary outline pill: 1px solid white or ink, radius about 22px, padding `8px 24px 10px`, weight 600. Examples: "Talk to our team", "Discover Focus".
- Header Login: white fill, ink text, radius about 30px, padding `4px 22px 6px`, weight 500.
- On dark bands use a white stroke. On light bands use an ink stroke. Flip label color for contrast.

**Navigation**
- Transparent header over the hero. White wordmark and links on dark.
- Primary nav: Focus, Studio, AI Visibility, Case Studies, News + Insights, About 3BL.

**Cards**
- Case study tiles: large photo plus title beside or over the image. No heavy bordered card chrome.
- Feature modules: four equal columns (Publish, Measure, Partner, Grow) with short headlines.

**Footer**
- Dark navy band. Link columns for Products, Who We Are, Media Brands, Legal. LinkedIn and Facebook icons.

## 5. Layout principles

- First viewport: brand, one headline, one supporting line, one CTA, one dominant product visual.
- Full-width bands with large vertical padding (section scale).
- Dashboard mockups sit inside dark product sections and act as the Focus hero image.
- Keep body measure readable. Headlines may span wider.

## 6. Depth and elevation

Mostly flat. Separate sections by swapping off-white and navy backgrounds. Soft shadow only under floating dashboard frames.

## 7. Do's and don'ts

**Do**
- Keep hero type at weight 300 and large. Use serif for narrative H2s.
- Match live-site pill outline CTAs.
- Show real product UI in Focus and Studio sections.

**Don't**
- Add purple or glow marketing effects.
- Pack dense stats into the first viewport beyond the dashboard visual.
- Use sharp 4px cards or Material-style FABs.

## 8. Responsive behavior

Fluid clamp type from hero through body. Nav collapses on mobile. CTAs stay full pills. Scale or crop dashboard imagery. Do not replace it with an empty abstract gradient.

## 9. Agent prompt guide

- "Build a 3bl.com-style section: `#F6FAFF` canvas, ink `#182334`, accent `#3687FF`, Plex Sans light hero and Plex Serif H2."
- "CTA: 22px pill, 1px outline, 15px/600 Plex Sans."
- "Alternate dark navy bands with light wash. Put dashboard UI mockups in dark product sections."
- "Eyebrows uppercase 13px. Login is a white pill in the header."
