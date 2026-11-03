# Vantage Sauna Co. · pitch package

Shared rooftop sauna suites for hotels, rental towers and condo buildings in **Vancouver, Victoria and Toronto**.
Vantage designs, factory-builds and installs the suites, then runs them on a service and booking subscription.

**Start here:** open [`index.html`](index.html), the landing page that links to everything below. On GitHub Pages
it is the home page of the site.

| | What | Open |
|---|---|---|
| 01 | Business plan (full written plan) | [`01-business-plan/`](01-business-plan/) · HTML, PDF, Markdown |
| 02 | Pitch deck with speaker notes | [`02-pitch-deck/`](02-pitch-deck/) · viewer (arrow keys, N for notes), PDF, slide source |
| 03 | Marketing website | [`03-website/index.html`](03-website/index.html) |
| 04 | 3D design plans, drawings and spec sheet | [`04-design-plans/index.html`](04-design-plans/index.html) |
| 05 | Financial model (Excel, live formulas) | [`05-financial-model/`](05-financial-model/) |
| 06 | Research (Canadian market, codes, costs; sauna design) | [`06-research/`](06-research/) |
| 07 | Project brief, the single source of truth | [`07-brief/BRIEF.md`](07-brief/BRIEF.md) |
| 08 | Launch plan: what to raise, startup costs, step-by-step plan | [`08-launch-plan/launch-plan.md`](08-launch-plan/launch-plan.md) |

## The plan in five lines

- **Raise about C$2.15M of equity**: C$150k pre-seed now and a C$2.0M seed by March 2027, plus a C$350k
  government-backed equipment loan and about C$150k of NRC IRAP support.
- **Launch in Vancouver and Victoria in 2027** (5 installs), **add Toronto in 2028**.
- **122 buildings by 2031** (about 11% of suitable buildings in the three cities), **C$9.2M revenue in 2031**.
- **EBITDA-positive from 2029**; cash never drops below C$0.84M in the base plan.
- Suites from **C$99,000** (Perch), C$179,000 (Lodge) and C$329,000 (Summit), installed, before tax.

## Updating the site

Edit the Markdown or slide files, then run:

```bash
./updateweb.sh "What changed"
```

The script rebuilds the HTML pages, the deck viewer and the PDFs (`tools/build.py`), commits everything and
pushes to GitHub. It warns before pushing to a public repository. Options: `--no-build` to skip the rebuild,
`--yes` to skip the warning. The first run creates a local `.venv` with the `markdown` package. PDFs need Google
Chrome.

To browse the package as a website, turn on GitHub Pages once: **Settings > Pages > Deploy from a branch >
main / (root)**. The site then lives at `https://<user>.github.io/<repo>/`.

To preview locally:

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

The 3D model loads Three.js from a CDN, so it needs an internet connection.

## How the pieces fit

1. Numbers are set once in `07-brief/BRIEF.md`.
2. The research in `06-research/` backs the brief; each claim links its source.
3. The Excel model turns the brief's assumptions into the P&L, cash flow and funding need.
4. The business plan, deck, website, design plans and launch plan all quote the same numbers.

The business plan, deck, website and design plans also exist as live, editable versions on claude.ai. Those links
work only for people they have been shared with; the copies in this repository work for everyone.

## Before you send this to anyone

- **This repository's visibility.** A public repository shows the financial model and research to everyone. To
  share with partners only, make it private (Settings > General > Change visibility) and add them as
  collaborators. GitHub Pages on a private repository needs a paid GitHub plan.
- Placeholders: founder surname and bio, contact details, advisers, and the seed valuation.
- "Vantage Sauna Co." and the model names Perch, Lodge and Summit are working names; a trademark search is step 1
  of the launch plan.

Figures are planning estimates. The design plans are design intent, not for construction.
