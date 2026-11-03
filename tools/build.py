#!/usr/bin/env python3
"""Build the static, shareable copies of the Vantage pitch package.

What it does
  * Renders the Markdown documents (business plan, brief, research) to styled HTML pages next to their sources.
  * Builds a standalone pitch-deck viewer (02-pitch-deck/index.html) from the Slides source in 02-pitch-deck/project.
  * With --pdf, prints the business plan and the deck to PDF using Google Chrome in headless mode.

Usage (from the repository root)
    pip install markdown
    python3 tools/build.py          # HTML only
    python3 tools/build.py --pdf    # HTML plus PDFs (needs Google Chrome)
"""
import argparse, html, json, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
try:
    import markdown
except ImportError:
    markdown = None
    print('The markdown package is not installed (pip install markdown): the Markdown pages keep their last build; the deck and PDFs are still rebuilt.')

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300..600&family=Inter:wght@400;500;600&display=swap">')

# (markdown source, html output, page title, short description) relative to ROOT
DOCS = [
    ('01-business-plan/business-plan.md', '01-business-plan/index.html', 'Business plan', 'The full business plan.'),
    ('07-brief/BRIEF.md', '07-brief/index.html', 'Project brief', 'The single source of truth every deliverable is built from.'),
    ('08-launch-plan/launch-plan.md', '08-launch-plan/index.html', 'Launch plan', 'How much to raise, what it costs to start, and the steps to launch.'),
]
RESEARCH_DIR = '06-research'
RESEARCH_TITLES = {
    'canada-market-research.md': ('Canadian market research', 'Hotels, condos and business apartments in Vancouver, Victoria and Toronto, with a sourced sizing.'),
    'canada-codes-and-engineering.md': ('Canadian codes and engineering', 'BC and Ontario building, electrical, seismic, snow-load and accessibility requirements.'),
    'canada-competition-and-costs.md': ('Canadian competition, costs and funding', 'Competitors, CAD cost inputs, wages, leases, grants and taxes.'),
    'sauna-design-research.md': ('Sauna design research', 'Existing products and precedents, heaters, benches, ventilation, glazing and code research.'),
}

def page(title, body, depth, extra_head=''):
    up = '../' * depth
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Vantage Sauna Co.</title>
{FONTS}
<link rel="stylesheet" href="{up}assets/docs.css">
{extra_head}
</head>
<body>
<header class="topbar"><div class="in">
  <a class="brand" href="{up}index.html"><span class="mark" aria-hidden="true"></span>Vantage Sauna Co.</a>
  <nav aria-label="Package"><a href="{up}index.html">All documents</a><a href="{up}01-business-plan/index.html">Business plan</a><a href="{up}08-launch-plan/index.html">Launch plan</a><a href="{up}02-pitch-deck/index.html">Pitch deck</a><a href="{up}04-design-plans/index.html">Design plans</a><a href="{up}03-website/index.html">Website</a></nav>
</div></header>
{body}
<footer class="site"><div class="in">Vantage Sauna Co. · Confidential pitch materials · Generated from Markdown by tools/build.py</div></footer>
</body>
</html>
'''

def render_markdown(src: Path, title: str, depth: int, downloads: str = '') -> str:
    md = markdown.Markdown(extensions=['tables', 'toc', 'fenced_code', 'sane_lists', 'attr_list'], extension_configs={'toc': {'toc_depth': '2-3'}})
    text = src.read_text(encoding='utf-8')
    # Charts in the live Claude Doc export as '[embedded content: caption]' placeholders; show them as a short note.
    text = re.sub(r'&#91;embedded content: (.*?)\\\]', r'> *Chart in the editable original (claude.ai). Data: \1.*', text)
    body = md.convert(text)
    body = re.sub(r'<table>', '<div class="table-wrap"><table>', body)
    body = body.replace('</table>', '</table></div>')
    toc = md.toc if md.toc_tokens else ''
    main = f'''<div class="layout">
<aside class="toc" aria-label="Contents"><p>Contents</p>{toc}</aside>
<article class="doc">
{downloads}
{body}
</article>
</div>'''
    return page(title, main, depth)

def build_docs():
    if markdown is None:
        return
    for src, dst, title, _ in DOCS:
        s, d = ROOT / src, ROOT / dst
        if not s.exists():
            print('skip (missing)', src); continue
        dl = ''
        if src.startswith('01-business-plan'):
            dl = '<div class="downloads"><a class="btn primary" href="business-plan.pdf">Download PDF</a><a class="btn" href="business-plan.md">Markdown source</a></div>'
        else:
            dl = f'<div class="downloads"><a class="btn" href="{s.name}">Markdown source</a></div>'
        d.write_text(render_markdown(s, title, dst.count('/'), dl), encoding='utf-8')
        print('wrote', dst)
    rdir = ROOT / RESEARCH_DIR
    cards = []
    for name in sorted(p.name for p in rdir.glob('*.md')):
        title, desc = RESEARCH_TITLES.get(name, (name[:-3].replace('-', ' ').capitalize(), ''))
        out = rdir / (name[:-3] + '.html')
        out.write_text(render_markdown(rdir / name, title, 1, f'<div class="downloads"><a class="btn" href="index.html">All research</a><a class="btn" href="{name}">Markdown source</a></div>'), encoding='utf-8')
        cards.append(f'<a class="card" href="{out.name}"><h2>{html.escape(title)}</h2><p>{html.escape(desc)}</p></a>')
        print('wrote', out.relative_to(ROOT))
    order = list(RESEARCH_TITLES)
    cards.sort(key=lambda c: next((i for i, k in enumerate(order) if k[:-3] + '.html' in c), 99))
    body = f'<div class="layout" style="grid-template-columns:1fr"><article class="doc" style="max-width:none"><h1>Research</h1><p class="meta">The sourced research behind the plan and the design. Each page links its sources.</p><div class="cards">{"".join(cards)}</div></article></div>'
    (rdir / 'index.html').write_text(page('Research', body, 1), encoding='utf-8')
    print('wrote', f'{RESEARCH_DIR}/index.html')

# ---------------------------------------------------------------- pitch deck viewer
ICONS = {  # stroke icons for the <x-icon> elements used in the Slides source
    'Home': '<path d="M3 11.5 12 4l9 7.5"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
    'Key': '<circle cx="8" cy="15" r="4"/><path d="m10.8 12.2 8.7-8.7"/><path d="m16 7 3 3"/><path d="m14 9 2 2"/>',
    'Lightning': '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    'Verified': '<path d="M12 2 4 6v6c0 5 3.5 8.5 8 10 4.5-1.5 8-5 8-10V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
    'Wrench': '<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L4 12l8-8z" transform="scale(.9) translate(1 1)"/>',
}
def icon_svg(m):
    attrs = m.group(1)
    name = re.search(r'name="([^"]+)"', attrs)
    style = re.search(r'style="([^"]*)"', attrs)
    paths = ICONS.get(name.group(1) if name else '', '<circle cx="12" cy="12" r="8"/>')
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="{style.group(1) if style else ""};display:block;flex-shrink:0" aria-hidden="true">{paths}</svg>'

DECK_CSS = '''
:root { --bg: #0F1A24; }
* { box-sizing: border-box; }
html, body { margin: 0; height: 100%; background: var(--bg); color: #F4EFE6; font-family: Inter, system-ui, sans-serif; }
.bar { position: fixed; inset: 0 0 auto 0; height: 52px; display: flex; align-items: center; gap: 12px; padding: 0 16px; background: rgba(15, 26, 36, .92); border-bottom: 1px solid rgba(220, 230, 232, .12); z-index: 5; font-size: 14px; }
.bar a, .bar button { color: #F4EFE6; background: transparent; border: 1px solid rgba(220, 230, 232, .25); border-radius: 999px; padding: 6px 12px; font: inherit; cursor: pointer; text-decoration: none; }
.bar .grow { flex: 1; }
.bar .count { font-variant-numeric: tabular-nums; color: #A9B1B7; }
.stage { position: fixed; inset: 52px 0 0 0; display: grid; place-items: center; overflow: hidden; }
.slide { position: absolute; width: 1920px; height: 1080px; transform-origin: center center; display: none; box-shadow: 0 20px 60px rgba(0, 0, 0, .45); }
.slide.on { display: block; }
.slide > section { position: relative; width: 1920px; height: 1080px; overflow: hidden; }
.slide section * { margin: 0; }
.slide section ul, .slide section ol { padding-left: 1.2em; }
.slide section table { border-collapse: collapse; width: 100%; }
.slide section th, .slide section td { padding: 14px 20px; vertical-align: top; }
.slide section b, .slide section strong { font-weight: 700; }
.slide section aside { display: none; }
.notes { position: fixed; left: 16px; right: 16px; bottom: 16px; max-height: 30vh; overflow: auto; background: rgba(15, 26, 36, .95); border: 1px solid rgba(220, 230, 232, .2); border-radius: 12px; padding: 12px 16px; font-size: 15px; line-height: 1.5; display: none; z-index: 6; }
.notes.on { display: block; }
.hint { color: #7D878F; font-size: 12.5px; }
@media (max-width: 640px) { .hint { display: none; } }
@media print {
  @page { size: 1920px 1080px; margin: 0; }
  html, body { height: auto; background: #fff; }
  .bar, .notes { display: none !important; }
  .stage { position: static; display: block; }
  .slide { position: relative; display: block !important; transform: none !important; box-shadow: none; break-after: page; page-break-after: always; }
}
'''
DECK_JS = '''
const slides = [...document.querySelectorAll('.slide')], notes = document.getElementById('notes'), count = document.getElementById('count');
let i = Math.max(0, Math.min(slides.length - 1, (parseInt(location.hash.slice(1), 10) || 1) - 1));
function fit() { const st = document.querySelector('.stage'); const k = Math.min(st.clientWidth / 1920, st.clientHeight / 1080) * 0.96; slides.forEach(s => s.style.transform = `scale(${k})`); }
function show(n) { i = Math.max(0, Math.min(slides.length - 1, n)); slides.forEach((s, j) => s.classList.toggle('on', j === i)); count.textContent = `${i + 1} / ${slides.length}`; const a = slides[i].querySelector('aside'); notes.textContent = a ? a.textContent : 'No speaker notes on this slide.'; history.replaceState(null, '', '#' + (i + 1)); }
document.getElementById('prev').onclick = () => show(i - 1);
document.getElementById('next').onclick = () => show(i + 1);
document.getElementById('toggle-notes').onclick = () => notes.classList.toggle('on');
document.addEventListener('keydown', e => { if (['ArrowRight', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); show(i + 1); } if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); show(i - 1); } if (e.key === 'n' || e.key === 'N') notes.classList.toggle('on'); if (e.key === 'Home') show(0); if (e.key === 'End') show(slides.length - 1); });
let x0 = null; document.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
document.addEventListener('touchend', e => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1)); x0 = null; });
window.addEventListener('resize', fit); window.addEventListener('hashchange', () => show((parseInt(location.hash.slice(1), 10) || 1) - 1)); fit(); show(i);
'''

def build_deck():
    proj = ROOT / '02-pitch-deck' / 'project'
    deck = json.loads((proj / 'deck.json').read_text(encoding='utf-8'))
    fonts = ''.join(f'<link rel="stylesheet" href="{html.escape(f["href"])}">' for f in deck.get('faces', {}).values())
    parts = []
    for sid in deck['order']:
        src = (proj / 'slides' / f'{sid}.html').read_text(encoding='utf-8')
        src = re.sub(r'<x-icon([^>]*)>\s*</x-icon>', icon_svg, src)
        src = re.sub(r'<x-icon([^>]*)/?>', icon_svg, src)
        parts.append(f'<div class="slide" data-id="{sid}">{src}</div>')
    title = html.escape(deck.get('title', 'Pitch deck'))
    out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{fonts}
<style>{DECK_CSS}</style>
</head>
<body>
<div class="bar">
  <a href="../index.html">All documents</a>
  <button type="button" id="prev" aria-label="Previous slide">‹</button>
  <span class="count" id="count"></span>
  <button type="button" id="next" aria-label="Next slide">›</button>
  <span class="grow"></span>
  <span class="hint">Arrow keys to move · N for speaker notes</span>
  <button type="button" id="toggle-notes">Notes</button>
  <a href="pitch-deck.pdf">PDF</a>
</div>
<main class="stage">
{''.join(parts)}
</main>
<div class="notes" id="notes" aria-live="polite"></div>
<script>{DECK_JS}</script>
</body>
</html>
'''
    (ROOT / '02-pitch-deck' / 'index.html').write_text(out, encoding='utf-8')
    print('wrote 02-pitch-deck/index.html', len(parts), 'slides')

# ---------------------------------------------------------------- PDFs
CHROME_CANDIDATES = ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', 'google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser']
def chrome():
    for c in CHROME_CANDIDATES:
        p = shutil.which(c) or (c if Path(c).exists() else None)
        if p: return p
    return None

def print_pdf(html_path: Path, pdf_path: Path):
    exe = chrome()
    if not exe:
        print('Chrome not found; skipping', pdf_path.name); return
    cmd = [exe, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=15000', '--run-all-compositor-stages-before-draw',
           f'--print-to-pdf={pdf_path}', html_path.resolve().as_uri()]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    print('wrote', pdf_path.relative_to(ROOT), f'{pdf_path.stat().st_size // 1024} KB')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pdf', action='store_true', help='also print PDFs with headless Chrome')
    ap.add_argument('--only', choices=['docs', 'deck'], help='build only the documents or only the deck')
    a = ap.parse_args()
    if a.only in (None, 'docs'): build_docs()
    if a.only in (None, 'deck'): build_deck()
    if a.pdf and a.only in (None, 'docs'): print_pdf(ROOT / '01-business-plan' / 'index.html', ROOT / '01-business-plan' / 'business-plan.pdf')
    if a.pdf and a.only in (None, 'deck'): print_pdf(ROOT / '02-pitch-deck' / 'index.html', ROOT / '02-pitch-deck' / 'pitch-deck.pdf')
