---
version: alpha
name: 3BL-media
description: "3blmedia.com. White newsroom, IBM Plex Sans and Serif, primary #3687FF for Subscribe and category labels (uppercase, 2px tracking). Serif feature headlines, dense feed with sidebar alerts, black footer."

colors:
  canvas: "#FFFFFF"
  ink: "#212529"
  ink-strong: "#000000"
  primary: "#3687FF"
  on-primary: "#FFFFFF"
  link: "#0066FF"
  footer: "#000000"
  on-footer: "#FFFFFF"

typography:
  h1:
    fontFamily: "IBM Plex Sans, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.2
  h2-feature:
    fontFamily: "IBM Plex Serif, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
  category:
    fontFamily: "IBM Plex Sans, sans-serif"
    fontSize: 14px
    fontWeight: 600
    letterSpacing: 2px
    textTransform: uppercase
    color: "#3687FF"
  body:
    fontFamily: "IBM Plex Sans, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  meta-link:
    fontFamily: "IBM Plex Sans, sans-serif"
    fontSize: 12px
    fontWeight: 500
    color: "#0066FF"

rounded:
  button: 8px
  card: 0px

spacing:
  feed-gap: 24px
  section: 48px
---

# Design system: 3BL Media (3blmedia.com)

> Live capture: https://www.3blmedia.com (agent-browser).
> Inherits: [`../common/DESIGN.md`](../common/DESIGN.md)

## 1. Visual theme and atmosphere

White page. Photography-led feature story, horizontal Trending Now cards, then a filtered vertical feed with a Recent Alerts sidebar. Blue is for Subscribe, category labels, and text links, not large washes. Serif for feature headlines. Sans for UI and body. Black footer.

## 2. Color palette and roles

| Role | Hex | Use |
|------|-----|-----|
| Canvas | `#FFFFFF` | Page background |
| Ink | `#212529` | Body, titles |
| Primary | `#3687FF` | Subscribe buttons, category labels |
| Link | `#0066FF` | "Read the full story", "More stories" |
| Footer | `#000000` | Footer band |

## 3. Typography rules

| Element | Spec |
|---------|------|
| Page H1 | Plex Sans 300 / 40px |
| Feature headline | Plex Serif 600 / about 32px |
| Category label | Plex Sans 600 / 14px / uppercase / letter-spacing 2px / `#3687FF` |
| Feed titles | Plex Sans bold |
| Body / dek | Plex Sans 16 / 400 |
| Meta links | Plex Sans 12 / 500 blue |

Primary fonts are IBM Plex Sans and Serif. Ignore incidental icon fonts.

## 4. Component stylings

**Subscribe CTA**
- Background `#3687FF`, white text, radius 8px, weight 700. Not marketing pills.

**Login**
- Text link, black, about 20px / 700. Not a filled button.

**Story cards (Trending)**
- Image on top, blue uppercase category, headline. No heavy card chrome.

**Feed rows**
- Thumbnail left, then category, headline, summary, date and company meta.

**Filters**
- Category and Media Type selects above the feed.

**Media brands band**
- Mid-page logos for 3BL Media, TriplePundit, CSRwire, ReportAlert, plus newsletter signup.

**Footer**
- Solid black. Get in touch and Solutions columns. Social icons.

## 5. Layout principles

Order: feature hero, trending rail, two-column feed (main plus alerts), brands, campaigns, footer. Dense layout. Category blue is the recurring accent. Use photographic journalism images.

## 6. Depth and elevation

Flat. Separate with whitespace and hairlines, not shadows. Buttons are solid fills without multi-layer shadow.

## 7. Do's and don'ts

**Do**
- Use blue uppercase category labels with 2px tracking.
- Pair Serif feature headlines with Sans UI.
- Keep Subscribe as the strongest filled blue control.

**Don't**
- Use a dark CSRwire-style canvas on this site.
- Default to 22px pill marketing CTAs from the corp site.
- Add purple or cream nostalgia themes.

## 8. Responsive behavior

Trending rail wraps or scrolls. Feed becomes one column. Sidebar alerts stack below. Subscribe stays in the header.

## 9. Agent prompt guide

- "3BL Media newsroom: white canvas, Plex Sans/Serif, Subscribe `#3687FF` 8px radius."
- "Category labels: uppercase 14px/600, letter-spacing 2px, blue."
- "Feature story: large photo and Plex Serif 32/600 headline."
- "Black footer. Blue text links for Read more."
