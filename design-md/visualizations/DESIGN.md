---
version: alpha
name: 3BL-visualizations
description: "Charts for 3BL Focus-style dashboards. Dark panels on near-black backgrounds, primary series #3687FF, mist and sage secondary series, thin gridlines. Matches 3bl.com dashboard mockups. Uses Gin neutrals when embedded in the client portal."

colors:
  stage: "#0B0F16"
  panel: "#182334"
  panel-elevated: "#1E2531"
  grid: "rgba(255,255,255,0.08)"
  axis: "#9DAABD"
  label: "#F1F1F0"
  label-muted: "#9DAABD"
  series-1: "#3687FF"
  series-2: "#98BCCD"
  series-3: "#93BEB5"
  series-4: "#7DB7FE"
  series-positive: "#AAFBAB"
  series-warning: "#d8b234"
  series-danger: "#cc3d3d"
  tooltip-bg: "#222330"
  tooltip-text: "#FFFFFF"
  light-stage: "#edeff5"
  light-panel: "#FFFFFF"
  light-axis: "#545560"
  light-grid: "rgba(34,35,48,0.08)"

typography:
  chart-title:
    fontFamily: IBM Plex Sans
    fontSize: 14px
    fontWeight: 600
  chart-label:
    fontFamily: IBM Plex Sans
    fontSize: 12px
    fontWeight: 400
  chart-metric:
    fontFamily: IBM Plex Sans
    fontSize: 28px
    fontWeight: 300
  chart-meta:
    fontFamily: IBM Plex Sans
    fontSize: 11px
    fontWeight: 500
    letterSpacing: 0.04em
    textTransform: uppercase

rounded:
  panel: 12px
  tooltip: 8px
---

# Design system: Visualizations

> From 3bl.com Focus dashboard mockups, Brand Guidelines accents, and Gin embed rules.
> Inherits: [`../common/DESIGN.md`](../common/DESIGN.md). Related: [`../client-portal/DESIGN.md`](../client-portal/DESIGN.md).

## 1. Visual theme and atmosphere

Dark panels, one blue series as the main series, muted supporting series, hairline grids. KPI numbers use IBM Plex Sans 300. Meta labels are small uppercase. In the Gin portal, switch to light embed tokens and keep the same series palette.

## 2. Color palette and roles

**Dark dashboard (marketing / Focus)**
| Role | Hex |
|------|-----|
| Stage | `#0B0F16` |
| Panel | `#182334` |
| Series primary | `#3687FF` |
| Series secondary | `#98BCCD` / `#93BEB5` / `#7DB7FE` |
| Positive | `#AAFBAB` |
| Axis / muted | `#9DAABD` |
| Labels | `#F1F1F0` |

**Light embed (Gin portal)**
| Role | Hex |
|------|-----|
| Stage | `#edeff5` |
| Panel | `#FFFFFF` |
| Axis | `#545560` |
| Series | same blues and sage |

Do not default to rainbow categorical palettes. Cap categorical color at 4 or 5 series from the brand set.

## 3. Typography rules

IBM Plex Sans only inside charts, even when Gin uses Inter for the shell. KPI: weight 300, about 28px or larger. Axis: 11 to 12px. Titles: 14px / 600. No serif inside chart plots.

## 4. Component stylings

- Panel card: 12px radius, dark fill, no heavy border, or 1px `rgba(255,255,255,0.06)`.
- Line charts: 2px strokes. Area fill at about 15% opacity of the series color.
- Bar charts: top radius about 2 to 4px. Primary blue bars. No 3D.
- Donut / gauge: thick muted track, value arc `#3687FF`, center metric at light weight.
- Radar: thin strokes, low fill, one highlighted series.
- Tooltip: `#222330` background, white text, 8px radius, no large shadow.
- Legend: horizontal, 12px labels, 8px swatches. Label series directly when there are 3 or fewer.

## 5. Layout principles

One chart answers one question. KPI plus sparkline pairs work in horizontal rails. Panel padding at least 16px. Align baselines across sibling cards. In the portal, constrain chart height and use responsive width, not fixed px.

## 6. Depth and elevation

Charts are flat. Panel elevation uses Gin L1 in the portal. Marketing mockups separate panel from stage by color only.

## 7. Do's and don'ts

**Do**
- Lead with `#3687FF` as the main series.
- Use mist and sage for comparison series.
- Label series directly when legends would clutter.

**Don't**
- Neon glow lines, gradient bars, or 3D pie charts.
- Mix random reds or purples unless the value is a status color.
- Put IBM Plex Serif on axis ticks.

## 8. Responsive behavior

Stack multi-card rails vertically. Hide secondary legends first. Keep the KPI. Tooltips work on tap. Point hit areas at least 24px.

## 9. Agent prompt guide

- "Dark Focus dashboard card: panel `#182334` on `#0B0F16`, series `#3687FF`, axis `#9DAABD`, Plex Sans metrics."
- "Portal embed: white panel on Gin `#edeff5`, same series blues."
- "KPI large light weight. Meta uppercase 11px."
- "Max 4 categorical colors from brand mist, sage, and blue."
