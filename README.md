# Vantage Sauna Co. — investor and sales package

Rooftop sauna suites, designed, built and installed for apartment buildings, hotels and offices.
Everything in this folder was built on 1 November 2026 from one source of truth, `BRIEF.md`.
Change a number there first, then propagate it.

## Deliverables

| Deliverable | Where | Notes |
|---|---|---|
| Business plan (17 sections, charts, sourced market analysis) | Claude Doc: https://claude.ai/artifact/1jg9X32pfVjARyWhqY1Sas | Edit inline, comment, export to Word/PDF from its Share menu. Markdown copy: `business-plan/business-plan.md` |
| Investor pitch deck (15 slides, speaker notes) | Slides artifact: https://claude.ai/artifact/GXeFrzGzpjB8D6vKRr4g3o | Downloads as .pptx or PDF from the deck page. Source files: `pitch-deck/project/` |
| Marketing website | `website/index.html` · published: https://claude.ai/artifact/2Y5n4dxsgFY6mtCPUTFXik | Lead form saves to the artifact database when published; mailto fallback when served locally |
| 3D design plans, 2D drawings, spec sheet | `design/index.html` · published: https://claude.ai/artifact/XS6wf21tNce8BkvgW6tzaQ | Three.js viewer; design intent only, not for construction |
| Five-year financial model | `financials/vantage-financial-model.xlsx` | 9 sheets, 1,121 live formulas, inputs in blue; recalculates on open in Excel |
| Market research fact base (sourced) | `research/market-research.md` | 24 opened sources, confidence ratings, deck-safe claims |
| Current-sauna product and design research | `research/sauna-design-research.md` | 15 products, 11 rooftop precedents, heaters, code, spec corrections |
| Source of truth | `BRIEF.md` | Brand, v2 specs, prices, recurring plans, five-year plan, funding, market |

## Run the website and design plans locally

```bash
cd /Users/jacob/Desktop/Vibe-coded/rooftop-sauna
python3 -m http.server 8080
# then open http://localhost:8080/website/  and  http://localhost:8080/design/
```

The 3D viewer loads Three.js from jsDelivr, so it needs an internet connection.

## Placeholders to fill before sending to anyone

- Founder surname and bio (deck slide 13, business plan "Team", deck cover and close).
- Contact email, phone and website on the closing slide; the website uses hello@vantagesauna.example.
- Advisor names as they confirm.
- Valuation and instrument for the seed round (deliberately left out).
- The company name "Vantage Sauna Co." and the model names Perch / Lodge / Summit are working names.

## Sharing

The Claude Doc and the Slides artifact are private until shared from each page's Share menu.
