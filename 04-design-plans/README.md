# Vantage rooftop sauna suites: design plans

`index.html` is a single self-contained page: the interactive 3D model, the scaled 2D drawings (plan, section, elevation), the wall and base build-up details, the spec sheet and the design notes for the Perch, Lodge and Summit suites. Everything on the page is generated from one dimension data object, so the 3D model, the drawings and the table cannot disagree with each other.

Audience: investors, building owners, and the engineers and sauna builders Vantage will hire. Status: **design intent, not for construction.**

Revision: **Rev P2, Canada (1 Nov 2026).** The package is drawn for Vancouver and Victoria (BC Building Code 2024 and the Vancouver Building By-law 2025) and Toronto (Ontario Building Code 2024). Prices are in Canadian dollars (C$) before GST/PST/HST. Facts come from `07-brief/BRIEF.md` (v4) and `06-research/canada-codes-and-engineering.md`; if they disagree, the brief wins.

## Serve it locally

From the project folder:

```sh
cd rooftop-sauna
python3 -m http.server 8080
```

Then open <http://localhost:8080/04-design-plans/>. Opening `04-design-plans/index.html` directly as a file also works in current browsers.

The page loads two external resources:

- Fraunces and Inter from Google Fonts (the page falls back to system serif and sans-serif faces without them).
- Three.js r160 (`three@0.160.0`) from cdn.jsdelivr.net as ES modules through an import map, for the 3D model only. Without network access the viewer shows a short notice and the drawings, details, spec sheet and notes keep working.

No build step, no other dependencies.

## What is on the page

1. **Header and controls.** Model switcher (Perch / Lodge / Summit, Lodge by default), metric / imperial toggle (rewrites every dimension on the page, including the 3D labels), light / dark toggle (remembered in `localStorage`). The model strip shows the installed from-price in C$.
2. **Sheet A-001, 3D model.** Orbit, zoom and pan; camera presets Exterior, Interior, Bench view, Plan (top), Section (the near side wall is clipped and the roof hidden); toggles for Night, Exploded view and Dimensions. The viewer stops auto-rotating on the first interaction and never auto-rotates when the OS asks for reduced motion.
3. **Sheets A-101 / A-201 / A-301.** Floor plan, cross-section A-A through the hot room and front elevation for the selected model, drawn to scale as inline SVG, with dimension strings, vent positions, drain, the 850 mm clear door and its swing, the ADA-style transfer bench (kept as best practice), its clear floor space and the 1,500 mm turning space (CSA B651). Title blocks carry the code basis (BCBC 2024 / VBBL 2025 / OBC 2024).
4. **Sheets A-501 / A-502.** Wall panel build-up (eight layers, outside to inside, with the noncombustible cladding option for towers in the notes) and the base frame in its two Canadian variants: **A, Toronto**, ballasted with no roof penetrations where the site is seismic category SC1 or SC2; **B, Vancouver and Victoria**, bolted to the structure through 4 to 8 engineered anchors, each in a factory-flashed curb sealed by the roofer (SC4: friction may not resist earthquake forces). Each has a short note on why.
5. **Sheet S-001.** Spec sheet for all three models; the selected model is highlighted. It covers the 850 mm door (950 mm leaf, Ontario glass-door strip), turning space, 208 V heaters with a Canadian mark (cETLus, cULus or CSA to CSA C22.2 No. 164), the hard-wired 1-hour no-override timer (Ontario OESC Rule 62-222), the 600 V transformer kit, fire and life safety (noncombustible cladding option, FRT or tested ceiling, sprinkler-ready, horn/strobe), the cold plunge as a regulated pool, both bases, loads (4.8 kPa occupied roof, 2.0 kPa module-roof snow, wind to NBC 4.1.7), delivery and crane permits, lead times (12–20 weeks, 16–26 for Summit) and the price breakdown with site preparation quoted separately. Electrical supplies are planning values at 208 V.
6. **Design notes and references.** Fourteen notes grounded in `06-research/canada-codes-and-engineering.md` and `06-research/sauna-design-research.md`, with the sources listed.
7. **Open items.** Eleven items for the engineer of record and the code consultant, including the new BC accessible-shower issue for the Lodge vestibule, the clear floor at the door, the glass front in an earthquake, and written interpretations of the 1-hour timer for app-started sessions.

## Editing the dimension data

Open `index.html` and find the block headed `VANTAGE SUITE DIMENSION DATA` near the top of the first `<script>`. Three objects drive everything:

- `SHARED`: the construction system common to all models. Wall thickness in plan (`wallPlan`) and the specified panel (`wallPanel`), floor and roof build-up thicknesses, roof pitch, base frame member depth and pad thickness, bench heights and depths (`bench`), door clear width and leaf (`door`: 850 mm clear, 950 mm leaf), turning space (`turning`: 1,500 mm), flat-pack panel limit (`panelMax`: 2.0 × 1.1 m, 120 kg), comfort volume per person, ventilation rate per person, the temperature cap, the eight wall layers (`wallLayers`) and the typical rooftop used in the 3D scene (`siteRoof`).
- `PRICING`: add-on prices and the site-preparation ranges (BC seismic anchorage and flashing, 600 V transformer kit), in C$.
- `MODELS`: one entry per model with the exterior footprint and height (`ext`), the hot room size and ceiling (`sauna`), the room `zones` along the depth (their depths must add up to `ext.d`), the heater count, rating and voltage, weights, ballast estimate (Toronto base), price and price breakdown (hardware, engineering and permits, delivery and install, electrical, commissioning), electrical supply and transformer size (`xfmrKva`), water, drain, delivery (`kit` true for the flat-pack default), lead time, plan label positions (`planLabels`), and the site pieces (outdoor shower, terrace deck, cold plunge).

Units are metres, kilograms, kilowatts, litres and Canadian dollars. Axes: x runs across the width from the gutter (low eave) side, z runs along the depth from the entry end, y is height above the roof surface. Change a value, save, reload: the model strip, the 3D model, all three drawings and the spec sheet update together. The derived geometry (bench rectangles, heater position, vent positions, base-frame feet, door swings, seat count, bearing pressure) is computed in `layout()` immediately below the data, and that is the place to change a layout rule rather than a number.

The exterior height in the brief is treated as the height to the high eave. The roof build-up is fixed at 180 mm at the low eave and rises 3 degrees across the width; the floor build-up is 100 mm; the base frame height is whatever remains, which is how the adjustable feet absorb the difference (Perch 194 mm, Lodge 163 mm, Summit 231 mm).

Drawing labels are masked: after each render (and after a units change or font load) `maskLabels()` puts a box the colour of the label's ground behind every label on the plan, section and detail sheets, so section marks, drains and dimension lines never strike through text. Give a label the class `on-floor`, `on-aspen` or `on-cool` when it sits on a room floor, a bench or a grating, and `nomask` when it sits on water or steel.

## Checking a change

- `node --check` on the two scripts (copy the first `<script>` block to a `.js` file and the `<script type="module">` block to a `.mjs` file).
- Headless Chrome: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --screenshot=out.png --window-size=1280,8000 http://localhost:8080/04-design-plans/`. Add `--use-angle=swiftshader --enable-unsafe-swiftshader` to render the WebGL model without a GPU.

## Caveat

This is a design intent package, not for construction. Structural, electrical and fire-code review by engineers licensed in BC (EGBC) or Ontario (PEO) is required for every site, with a code consultant's opinion where the building official has to interpret the code. Imperial values are converted from the metric design values; the nominal 8′ × 10′, 10′ × 16′ and 12′ × 24′ footprints in marketing copy are rounded.
