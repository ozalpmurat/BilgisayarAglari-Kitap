# AGENTS.md - Project Development Guide

This document contains non-obvious information about the Bilgisayar Ağları (Computer Networks) MkDocs documentation project.

## Build & Development Commands

```bash
# Local development server with live reload (a ready virtualenv lives in ./env)
source env/bin/activate
mkdocs serve

# Build static site
mkdocs build

# Build with PDF export (requires ENABLE_PDF_EXPORT env var)
ENABLE_PDF_EXPORT=1 mkdocs build

# Install dependencies
pip install -r requirements.txt
```

## Architecture

### Deployment
The site is built and deployed by a **single** workflow: [`.github/workflows/DeployGitHubPages.yml`](.github/workflows/DeployGitHubPages.yml). On every push to `main`/`master` that touches `docs/**`, `includes/**`, `requirements.txt` or `mkdocs.yml`, it runs `mkdocs build`, uploads the `site/` directory as a Pages artifact and deploys it to GitHub Pages. Actions are pinned to their current major versions (`checkout@v7`, `setup-python@v7`, `configure-pages@v6`, `upload-pages-artifact@v5`, `deploy-pages@v5`).

[`Github/Workflows/`](Github/Workflows) holds two older workflows (`mkdocs-deploy-GithubPages01/02.yml`). They are **not** in `.github/workflows/`, so GitHub never runs them; treat them as history, not as configuration.

### PDF Export Pipeline
- Enabled via `ENABLE_PDF_EXPORT=1` environment variable (set in the workflow, so every CI build also produces a PDF)
- Output: `site/BilgisayarAglari-MuratÖzalp.pdf`
- Published **with the site**, not attached to a GitHub Release: the release-upload step is commented out in the workflow, and `docs/index.md` + `README.md` link to the PDF served from GitHub Pages
- Cover includes "Bilecik Şeyh Edebali Üniversitesi" branding
- A very large image can break PDF generation; keep big diagrams reasonably sized

## Key Plugins & Extensions

### Enabled Plugins
- `mkdocs-material` - Material theme, configured with `locale: tr` (no Turkish translation bundle exists)
- `mkdocs-video` - Video embedding support
- `mkdocs-with-pdf` - PDF generation (conditional)
- `mkdocs-print-site-plugin` - Print-friendly site generation
- `mkdocs_pymdownx_material_extras` - Additional Material theme features

### Custom Markdown Extensions
- **Math support**: `pymdownx.arithmatex` (generic mode; `block_tag` stays at its default)
- **Mermaid diagrams**: `pymdownx.superfences` configured for Mermaid
- **Auto-abbreviations**: `includes/abbreviations.md` auto-appended via `pymdownx.snippets`

### Unused/Experimental Plugins
These are configured but commented out in [`mkdocs.yml`](mkdocs.yml):
- `mkdocs-mermaid2-plugin` - Mermaid diagram support
- `mkdocs-plantuml` - PlantUML diagrams
- `glightbox` - Image lightbox

## Localization

### Turkish Configuration
- **Theme locale**: `tr` (Material has no `tr` translation bundle, so `mkdocs build` always warns `No translations could be found for the locale 'tr'`; it is harmless)
- **Timezone**: not set in CI; the runner is UTC, so timestamps in the generated PDF are UTC
- **Search**: Turkish language (`search.lang: tr`)
- **Site**: Turkish content ("Bilgisayar Ağları Ders Notları")

## Custom Patterns

### Abbreviation System
The [`includes/abbreviations.md`](includes/abbreviations.md) file provides auto-expanding abbreviations. Notably:
- `[XXX]` - Special marker indicating unfinished sections needing review (the abbreviation is defined, but currently no page uses it)
- All networking terms (OSI, CIA, LAN, MAN, PAN, VLAN, WAN, NAT, MOBESE, etc.)

### No custom CSS
Heading permalinks (`¶`) are rendered by the theme itself and already appear on hover, so no `extra_css` is configured. `docs_dir` is `docs/`, therefore a stylesheet must live inside `docs/` to be copied into the build.

### Live Reload Watching
The `watch` configuration in [`mkdocs.yml`](mkdocs.yml:9) monitors the `includes/` directory for changes during development.

## Content Structure

### Chapter Organization
- `docs/02-Topolojiler.md` through `docs/11-Ag_izleme_ve_Yonetim.md` - Sequential chapters
- `docs/99-Deneme_tahtasi.md` - Scratch/sandbox page for experiments
- All images in `docs/images/` organized by chapter prefix (B02, B03, etc.)

### Image Conventions
- Diagrams use Excalidraw format (`.excalidraw` files)
- Large images (topology diagrams) exceed 200KB
- Some images are intentionally humorous (e.g., `B03-iletisim_komik.png`, `B03-TCPveUDP-Komik.png`)

## CI/CD Environment Variables

| Variable | Purpose |
|----------|---------|
| `ENABLE_PDF_EXPORT` | Enables PDF generation; the workflow sets it to `1`, it is unset locally by default |

No `TZ` or `locale` variables are set in CI. The Turkish locale comes from `theme.locale: tr` in `mkdocs.yml`.

## Google Analytics

The site uses Google Analytics with property ID: `G-QTZXBE6Z2Z`

## Known Quirks

1. **No `nav`**: page order comes from the numeric filename prefix (`02-`, `03-`, …) and each file name also becomes its URL. Renaming a chapter changes both.
2. **Keep `docs/` clean**: every `.md` file under `docs/` is built as a page. A leftover file such as `10-... copy.md` shows up as `/10-Yerel_Aglarda_Guvenlik%20copy/`.
3. **Images**: link them as `images/<file>` from a chapter in `docs/`; a `B*` prefix alone is not enough, and a wrong path fails silently as a broken image (build only warns).
4. **PDF filename encoding**: Contains Turkish characters (`BilgisayarAglari-MuratÖzalp.pdf`)
5. **Material theme sidebar**: Disabled (`include_sidebar: false`)
6. **Mermaid**: works out of the box. Material loads `https://unpkg.com/mermaid@11/dist/mermaid.min.js` at runtime and renders every `.mermaid` block into a **closed shadow root**, so the diagram is invisible to `curl`, text extraction and the HTML source (you only see `<pre class="mermaid">`). Check it in a real browser. The PDF does **not** run JavaScript, so Mermaid blocks stay as raw code there.
7. **Math**: MathJax 3 is loaded from jsDelivr; the `polyfill.io` script is commented out.
8. **Harmless build warnings**: `No translations could be found for the locale 'tr'` and `Template skipped: 'sitemap.html' not found in theme directories`.
9. **Workflow triggers**: the deploy runs only when `docs/**`, `includes/**`, `requirements.txt` or `mkdocs.yml` change. A commit that only touches `AGENTS.md` or the workflow file does not deploy — use *Run workflow* (workflow_dispatch) to test it.
