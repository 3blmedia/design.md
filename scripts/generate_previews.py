#!/usr/bin/env python3
"""Generate preview-light.html and preview-dark.html from each DESIGN.md frontmatter."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DESIGN_MD = ROOT / "design-md"

# Per-product light/dark token picks when keys are not generic.
THEMES: dict[str, dict[str, dict[str, str]]] = {
    "common": {
        "light": {
            "canvas": "wash",
            "ink": "ink",
            "muted": "slate-muted",
            "primary": "primary",
            "on-primary": "on-primary",
            "surface": "white",
            "border": "slate-muted",
            "accent-2": "mist",
            "accent-3": "sage",
        },
        "dark": {
            "canvas": "ink",
            "ink": "wash",
            "muted": "slate-muted",
            "primary": "primary",
            "on-primary": "on-primary",
            "surface": "slate",
            "border": "slate",
            "accent-2": "mist",
            "accent-3": "sage",
        },
    },
    "corp-website": {
        "light": {
            "canvas": "canvas",
            "ink": "ink",
            "muted": "cookie-slate",
            "primary": "primary",
            "on-primary": "on-primary",
            "surface": "white",
            "border": "primary-light",
            "accent-2": "primary-light",
            "accent-3": "economy",
        },
        "dark": {
            "canvas": "ink",
            "ink": "white",
            "muted": "primary-light",
            "primary": "primary",
            "on-primary": "on-primary",
            "surface": "cookie-slate",
            "border": "cookie-slate",
            "accent-2": "primary-light",
            "accent-3": "economy",
        },
    },
    "client-portal": {
        "light": {
            "canvas": "bg-layer2",
            "ink": "text",
            "muted": "text-light",
            "primary": "focus",
            "on-primary": "bg-layer",
            "surface": "bg-layer",
            "border": "border",
            "accent-2": "brand-primary",
            "accent-3": "success",
        },
        "dark": {
            "canvas": "title",
            "ink": "bg-layer",
            "muted": "border",
            "primary": "brand-primary",
            "on-primary": "bg-layer",
            "surface": "icon",
            "border": "text-light",
            "accent-2": "focus",
            "accent-3": "success",
        },
    },
    "visualizations": {
        "light": {
            "canvas": "light-stage",
            "ink": "light-axis",
            "muted": "axis",
            "primary": "series-1",
            "on-primary": "tooltip-text",
            "surface": "light-panel",
            "border": "axis",
            "accent-2": "series-2",
            "accent-3": "series-3",
        },
        "dark": {
            "canvas": "stage",
            "ink": "label",
            "muted": "axis",
            "primary": "series-1",
            "on-primary": "tooltip-text",
            "surface": "panel",
            "border": "panel-elevated",
            "accent-2": "series-2",
            "accent-3": "series-3",
        },
    },
    "3blmedia": {
        "light": {
            "canvas": "canvas",
            "ink": "ink",
            "muted": "ink",
            "primary": "primary",
            "on-primary": "on-primary",
            "surface": "canvas",
            "border": "link",
            "accent-2": "link",
            "accent-3": "primary",
        },
        "dark": {
            "canvas": "footer",
            "ink": "on-footer",
            "muted": "link",
            "primary": "primary",
            "on-primary": "on-primary",
            "surface": "ink-strong",
            "border": "ink",
            "accent-2": "link",
            "accent-3": "primary",
        },
    },
    "csrwire": {
        "light": {
            "canvas": "ra-canvas",
            "ink": "ra-ink",
            "muted": "ra-blue",
            "primary": "ra-hover",
            "on-primary": "ra-canvas",
            "surface": "ra-canvas",
            "border": "ra-blue",
            "accent-2": "ra-nav",
            "accent-3": "mist",
        },
        "dark": {
            "canvas": "csr-stage",
            "ink": "csr-text",
            "muted": "csr-link",
            "primary": "csr-link",
            "on-primary": "csr-stage",
            "surface": "csr-panel",
            "border": "csr-panel",
            "accent-2": "csr-wash",
            "accent-3": "economy",
        },
    },
}

FONT_STACKS: dict[str, str] = {
    "common": "'IBM Plex Sans', system-ui, sans-serif",
    "corp-website": "'IBM Plex Sans', system-ui, sans-serif",
    "client-portal": "Inter, system-ui, sans-serif",
    "visualizations": "'IBM Plex Sans', system-ui, sans-serif",
    "3blmedia": "'IBM Plex Sans', system-ui, sans-serif",
    "csrwire": "'IBM Plex Sans', system-ui, sans-serif",
}

SERIF_STACKS: dict[str, str] = {
    "common": "'IBM Plex Serif', Georgia, serif",
    "corp-website": "'IBM Plex Serif', Georgia, serif",
    "client-portal": "Georgia, serif",
    "visualizations": "'IBM Plex Sans', system-ui, sans-serif",
    "3blmedia": "'IBM Plex Serif', Georgia, serif",
    "csrwire": "'IBM Plex Serif', Georgia, serif",
}

GOOGLE_FONTS = (
    "https://fonts.googleapis.com/css2?"
    "family=IBM+Plex+Sans:wght@300;400;500;600;700&"
    "family=IBM+Plex+Serif:wght@400;500;600&"
    "family=Inter:wght@400;500;600;700&display=swap"
)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError(f"No YAML frontmatter in {path}")
    data = yaml.safe_load(match.group(1)) or {}
    return data


def resolve(colors: dict, key: str, fallback: str = "#888888") -> str:
    if key not in colors:
        return fallback
    value = colors[key]
    if isinstance(value, str) and value.startswith("#"):
        return value
    if isinstance(value, str) and value.startswith("rgb"):
        return value
    return str(value)


def build_theme(slug: str, mode: str, colors: dict) -> dict[str, str]:
    mapping = THEMES[slug][mode]
    return {role: resolve(colors, token) for role, token in mapping.items()}


def swatch_rows(colors: dict) -> str:
    items = []
    for name, value in colors.items():
        if not isinstance(value, str):
            continue
        if not (value.startswith("#") or value.startswith("rgb")):
            continue
        items.append(
            f'<div class="swatch"><div class="chip" style="background:{value}"></div>'
            f"<div><code>{name}</code><span>{value}</span></div></div>"
        )
    return "\n".join(items)


def render_html(
    *,
    slug: str,
    mode: str,
    meta: dict,
    colors: dict,
    theme: dict[str, str],
) -> str:
    name = meta.get("name", slug)
    description = meta.get("description", "")
    title = f"{name} · preview-{mode}"
    font = FONT_STACKS[slug]
    serif = SERIF_STACKS[slug]
    swatches = swatch_rows(colors)
    other = "dark" if mode == "light" else "light"

    return f"""<!DOCTYPE html>
<html lang="en" data-mode="{mode}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{GOOGLE_FONTS}" rel="stylesheet" />
  <style>
    :root {{
      --canvas: {theme["canvas"]};
      --ink: {theme["ink"]};
      --muted: {theme["muted"]};
      --primary: {theme["primary"]};
      --on-primary: {theme["on-primary"]};
      --surface: {theme["surface"]};
      --border: {theme["border"]};
      --accent-2: {theme["accent-2"]};
      --accent-3: {theme["accent-3"]};
      --font: {font};
      --serif: {serif};
      --radius: 12px;
      --radius-pill: 22px;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: var(--font);
      background: var(--canvas);
      color: var(--ink);
      line-height: 1.5;
    }}
    header.hero {{
      padding: 48px 32px 32px;
      border-bottom: 1px solid color-mix(in srgb, var(--border) 55%, transparent);
    }}
    .eyebrow {{
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      margin: 0 0 8px;
    }}
    h1 {{
      font-family: var(--serif);
      font-size: clamp(28px, 4vw, 44px);
      font-weight: 500;
      line-height: 1.15;
      margin: 0 0 12px;
      max-width: 18ch;
    }}
    .desc {{
      max-width: 62ch;
      color: var(--muted);
      margin: 0 0 20px;
    }}
    .meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }}
    .pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: 999px;
      border: 1px solid color-mix(in srgb, var(--border) 70%, transparent);
      font-size: 12px;
      color: var(--muted);
      text-decoration: none;
    }}
    .pill strong {{ color: var(--ink); font-weight: 600; }}
    main {{
      padding: 32px;
      display: grid;
      gap: 40px;
      max-width: 1100px;
    }}
    section h2 {{
      font-size: 14px;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      margin: 0 0 16px;
      color: var(--muted);
    }}
    .swatches {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 12px;
    }}
    .swatch {{
      display: flex;
      gap: 10px;
      align-items: center;
      padding: 10px;
      background: var(--surface);
      border: 1px solid color-mix(in srgb, var(--border) 50%, transparent);
      border-radius: 10px;
    }}
    .chip {{
      width: 40px;
      height: 40px;
      border-radius: 8px;
      border: 1px solid color-mix(in srgb, var(--ink) 12%, transparent);
      flex: none;
    }}
    .swatch code {{
      display: block;
      font-size: 12px;
      color: var(--ink);
    }}
    .swatch span {{
      font-size: 11px;
      color: var(--muted);
    }}
    .type-row {{
      display: grid;
      gap: 18px;
    }}
    .type-sample .label {{
      font-size: 11px;
      color: var(--muted);
      margin-bottom: 4px;
    }}
    .display {{
      font-family: var(--font);
      font-size: clamp(40px, 7vw, 72px);
      font-weight: 300;
      letter-spacing: -0.03em;
      line-height: 0.95;
    }}
    .headline {{
      font-family: var(--serif);
      font-size: 32px;
      font-weight: 600;
      line-height: 1.2;
    }}
    .body {{
      font-size: 16px;
      max-width: 60ch;
    }}
    .caption {{
      font-size: 12px;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--muted);
      font-weight: 600;
    }}
    .row {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
    }}
    .btn {{
      appearance: none;
      border: 0;
      cursor: pointer;
      font: inherit;
      font-size: 14px;
      font-weight: 600;
      padding: 10px 18px;
      border-radius: var(--radius-pill);
    }}
    .btn-primary {{
      background: var(--primary);
      color: var(--on-primary);
    }}
    .btn-outline {{
      background: transparent;
      color: var(--ink);
      border: 1px solid var(--ink);
    }}
    .btn-ghost {{
      background: transparent;
      color: var(--primary);
      border: 1px solid var(--primary);
    }}
    .btn-soft {{
      background: var(--surface);
      color: var(--ink);
      border: 1px solid color-mix(in srgb, var(--border) 70%, transparent);
      border-radius: 8px;
    }}
    .cards {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
    }}
    .card {{
      background: var(--surface);
      border: 1px solid color-mix(in srgb, var(--border) 55%, transparent);
      border-radius: var(--radius);
      padding: 18px;
    }}
    .card h3 {{
      margin: 0 0 8px;
      font-size: 18px;
      font-family: var(--serif);
      font-weight: 600;
    }}
    .card p {{
      margin: 0;
      color: var(--muted);
      font-size: 14px;
    }}
    .bars {{
      display: grid;
      gap: 10px;
      max-width: 420px;
    }}
    .bar {{
      height: 12px;
      border-radius: 999px;
      background: color-mix(in srgb, var(--border) 35%, transparent);
      overflow: hidden;
    }}
    .bar > span {{
      display: block;
      height: 100%;
      border-radius: inherit;
    }}
    .inputs {{
      display: grid;
      gap: 12px;
      max-width: 360px;
    }}
    label {{
      display: grid;
      gap: 6px;
      font-size: 13px;
      font-weight: 500;
    }}
    input, select {{
      font: inherit;
      padding: 10px 12px;
      border-radius: 8px;
      border: 1px solid color-mix(in srgb, var(--border) 80%, transparent);
      background: var(--surface);
      color: var(--ink);
    }}
    input:focus, select:focus {{
      outline: 2px solid color-mix(in srgb, var(--primary) 55%, transparent);
      outline-offset: 1px;
    }}
    footer {{
      padding: 24px 32px 48px;
      color: var(--muted);
      font-size: 12px;
    }}
    footer a {{ color: var(--primary); }}
  </style>
</head>
<body>
  <header class="hero">
    <p class="eyebrow">{slug} · preview-{mode}</p>
    <h1>{name}</h1>
    <p class="desc">{description}</p>
    <div class="meta">
      <span class="pill"><strong>Mode</strong> {mode}</span>
      <a class="pill" href="./preview-{other}.html">Open preview-{other}</a>
      <a class="pill" href="./DESIGN.md">DESIGN.md</a>
    </div>
  </header>
  <main>
    <section>
      <h2>Colors</h2>
      <div class="swatches">
{swatches}
      </div>
    </section>

    <section>
      <h2>Typography</h2>
      <div class="type-row">
        <div class="type-sample">
          <div class="label">Display / 300</div>
          <div class="display">Your story deserves more</div>
        </div>
        <div class="type-sample">
          <div class="label">Headline / serif 600</div>
          <div class="headline">We help companies tell stories that build trust.</div>
        </div>
        <div class="type-sample">
          <div class="label">Body / 400</div>
          <p class="body">Distribute corporate content to credible publishers. Track performance. Extend your team with guidance that improves the next update.</p>
        </div>
        <div class="type-sample">
          <div class="label">Caption / uppercase</div>
          <div class="caption">Our products · Focus · Studio</div>
        </div>
      </div>
    </section>

    <section>
      <h2>Buttons</h2>
      <div class="row">
        <button class="btn btn-primary" type="button">Primary action</button>
        <button class="btn btn-outline" type="button">Outline</button>
        <button class="btn btn-ghost" type="button">Ghost</button>
        <button class="btn btn-soft" type="button">Soft</button>
      </div>
    </section>

    <section>
      <h2>Cards</h2>
      <div class="cards">
        <article class="card">
          <p class="caption">Publish</p>
          <h3>Reach real audiences</h3>
          <p>Trusted channels where decision-makers already pay attention.</p>
        </article>
        <article class="card">
          <p class="caption">Measure</p>
          <h3>Track performance</h3>
          <p>Realtime dashboard, custom reports, peer benchmarks.</p>
        </article>
        <article class="card">
          <p class="caption">Partner</p>
          <h3>Extend your team</h3>
          <p>Client success works beside yours on the next story.</p>
        </article>
      </div>
    </section>

    <section>
      <h2>Series / accents</h2>
      <div class="bars">
        <div class="bar"><span style="width:78%;background:var(--primary)"></span></div>
        <div class="bar"><span style="width:56%;background:var(--accent-2)"></span></div>
        <div class="bar"><span style="width:34%;background:var(--accent-3)"></span></div>
      </div>
    </section>

    <section>
      <h2>Form</h2>
      <div class="inputs">
        <label>Email
          <input type="email" placeholder="you@company.com" />
        </label>
        <label>Product
          <select>
            <option>Focus</option>
            <option>Studio</option>
            <option>AI Visibility</option>
          </select>
        </label>
      </div>
    </section>
  </main>
  <footer>
    Generated from DESIGN.md frontmatter for <strong>{slug}</strong>.
    Source: <a href="./DESIGN.md">DESIGN.md</a>
  </footer>
</body>
</html>
"""


def main() -> None:
    for path in sorted(DESIGN_MD.glob("*/DESIGN.md")):
        slug = path.parent.name
        if slug not in THEMES:
            print(f"skip {slug}: no theme map")
            continue
        meta = parse_frontmatter(path)
        colors = meta.get("colors") or {}
        for mode in ("light", "dark"):
            theme = build_theme(slug, mode, colors)
            html = render_html(
                slug=slug,
                mode=mode,
                meta=meta,
                colors=colors,
                theme=theme,
            )
            out = path.parent / f"preview-{mode}.html"
            out.write_text(html, encoding="utf-8")
            print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
