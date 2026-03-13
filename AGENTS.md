# AGENTS.md - Project Development Guide

This document contains non-obvious information about the Bilgisayar Ağları (Computer Networks) MkDocs documentation project.

## Build & Development Commands

```bash
# Local development server with live reload
mkdocs serve

# Build static site
mkdocs build

# Build with PDF export (requires ENABLE_PDF_EXPORT env var)
ENABLE_PDF_EXPORT=1 mkdocs build

# Install dependencies
pip install -r requirements.txt
```

## Architecture

### Dual Deployment Strategy
The project uses **two separate GitHub Actions workflows** for deployment:

1. **[`mkdocs-deploy-GithubPages01.yml`](Github/Workflows/mkdocs-deploy-GithubPages01.yml)** - Uses `ldeluigi/markdown-docs` generator, simpler but no PDF support
2. **[`mkdocs-deploy-GithubPages02.yml`](Github/Workflows/mkdocs-deploy-GithubPages02.yml)** - Uses standard `mkdocs build` with PDF generation and automatic PDF upload to GitHub Releases

### PDF Export Pipeline
- Enabled via `ENABLE_PDF_EXPORT=1` environment variable
- Output: `site/BilgisayarAglari-MuratÖzalp.pdf`
- Generated during CI/CD and automatically uploaded as a release asset
- Cover includes "Bilecik Şeyh Edebali Üniversitesi" branding

## Key Plugins & Extensions

### Enabled Plugins
- `mkdocs-material` - Material theme with Turkish localization
- `mkdocs-video` - Video embedding support
- `mkdocs-with-pdf` - PDF generation (conditional)
- `mkdocs-print-site-plugin` - Print-friendly site generation
- `mkdocs_pymdownx_material_extras` - Additional Material theme features

### Custom Markdown Extensions
- **Math support**: `pymdownx.arithmatex` (generic mode, block tag: `pre`)
- **Mermaid diagrams**: `pymdownx.superfences` configured for Mermaid
- **Auto-abbreviations**: `includes/abbreviations.md` auto-appended via `pymdownx.snippets`

### Unused/Experimental Plugins
These are configured but commented out in [`mkdocs.yml`](mkdocs.yml):
- `mkdocs-mermaid2-plugin` - Mermaid diagram support
- `mkdocs-plantuml` - PlantUML diagrams
- `glightbox` - Image lightbox

## Localization

### Turkish Configuration
- **Timezone**: `Europe/Istanbul` (set in GitHub Actions)
- **Locale**: `tr` (Turkish)
- **Search**: Turkish language (`search.lang: tr`)
- **Site**: Turkish content ("Bilgisayar Ağları Ders Notları")

## Custom Patterns

### Abbreviation System
The [`includes/abbreviations.md`](includes/abbreviations.md) file provides auto-expanding abbreviations. Notably:
- `[XXX]` - Special marker indicating unfinished sections needing review
- All networking terms (OSI, CIA, LAN, VLAN, WAN, NAT, etc.)

### Custom CSS
The [`css/extra.css`](css/extra.css) file provides hover-reveal anchor links for all headings - anchors become visible only on hover.

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
| `ENABLE_PDF_EXPORT` | Enables PDF generation (set in workflow) |
| `TZ` / `timezone` | Europe/Istanbul for consistent timestamps |
| `locale` | Turkish locale settings |

## Google Analytics

The site uses Google Analytics with property ID: `G-QTZXBE6Z2Z`

## Known Quirks

1. **Dual workflow execution**: Both workflows trigger on push to `main`, but only one should run to avoid conflicts (concurrency group: `pages`)
2. **PDF filename encoding**: Contains Turkish characters (`BilgisayarAglari-MuratÖzalp.pdf`)
3. **Material theme sidebar**: Disabled (`include_sidebar: false`)
4. **Mermaid loading**: CDN JavaScript for Mermaid is commented out - relies on browser polyfill for ES6 features
5. **MathJax fallback**: Uses `polyfill.io` as JavaScript polyfill, MathJax 3 for math rendering
