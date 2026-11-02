# Vantage rooftop sauna suites: design plans

`index.html` is a single self-contained page: the interactive 3D model, the scaled 2D drawings (plan, section, elevation), the wall and base build-up details, the spec sheet and the design notes for the Perch, Lodge and Summit suites. Everything on the page is generated from one dimension data object, so the 3D model, the drawings and the table cannot disagree with each other.

Audience: investors, building owners, and the engineers and sauna builders Vantage will hire. Status: **design intent, not for construction.**

## Serve it locally

From the project folder:

```sh
cd rooftop-sauna
python3 -m http.server 8000
```

Then open <http://localhost:8000/design/>. Opening `design/index.html` directly as a file also works in current browsers.

The page loads two external resources:

- Fraunces and Inter from Google Fonts (the page falls back to system serif and sans-serif faces without them).
- Three.js r160 (`three@0.160.0`) from cdn.jsdelivr.net as ES modules through an import map, for the 3D model only. Without network access the viewer shows a short notice and the drawings, details, spec sheet and notes keep working.

No build step, no other dependencies. The file is about 170 KB.

## What is on the page

1. **Header and controls.** Model switcher (Perch / Lodge / Summit, Lodge by default), metric / imperial toggle (rewrites every dimension on the page, including the 3D labels), light / dark toggle (remembered in `localStorage`).
2. **Sheet A-001, 3D model.** Orbit, zoom and pan; camera presets Exterior, Interior, Plan (top), Section (the near side wall is clipped and the roof hidden); toggles for Night (dim sky, interior glow), Exploded view (base frame, floor, benches and heater, wall panels, roof, with labels) and Dimensions (overall width, depth, height, bench heights, ceiling). The viewer stops auto-rotating on the first interaction and never auto-rotates when the OS asks for reduced motion.
3. **Sheets A-101 / A-201 / A-301.** Floor plan, cross-section A-A through the hot room and front elevation for the selected model, drawn to scale as inline SVG, with dimension strings, vent positions, drain, door swings, the ADA transfer bench, its clear floor space and the 1,525 mm turning circle.
4. **Sheets A-501 / A-502.** Wall panel build-up (eight layers, outside to inside) and the base frame on pads with ballast tray and parapet tie-back, each with a short note on why.
5. **Sheet S-001.** Spec sheet for all three models; the selected model is highlighted. Electrical supplies are planning values.
6. **Design notes and references.** Twelve notes grounded in `research/sauna-design-research.md`, with the sources listed.
7. **Open items.** Five items the engineer of record must settle before production drawings: wall thickness versus footprint, seat places versus headline ranges, Summit effective volume, heater clearances, and point loads.

## Editing the dimension data

Open `index.html` and find the block headed `VANTAGE SUITE DIMENSION DATA` near the top of the first `<script>`. Two objects drive everything:

- `SHARED`: the construction system common to all models. Wall thickness in plan (`wallPlan`) and the specified panel (`wallPanel`), floor and roof build-up thicknesses, roof pitch, base frame member depth and pad thickness, bench heights and depths (`bench`), door clear width and leaf, turning circle, comfort volume per person, ventilation rate per person, the temperature cap, the eight wall layers (`wallLayers`) and the typical rooftop used in the 3D scene (`siteRoof`).
- `MODELS`: one entry per model with the exterior footprint and height (`ext`), the hot room size and ceiling (`sauna`), the room `zones` along the depth (their depths must add up to `ext.d`), which end the glass front faces (`saunaFront`), the heater count and rating, where the sauna door sits (`saunaDoor.u0`, measured along the wall from the gutter side), the entry door, weights, ballast estimate, price and price breakdown, electrical, water, drain, delivery and programme values, and the site pieces (outdoor shower, terrace deck, cold plunge).

Units are metres, kilograms, kilowatts, litres and US dollars. Axes: x runs across the width from the gutter (low eave) side, z runs along the depth from the entry end, y is height above the roof surface. Change a value, save, reload: the model strip, the 3D model, all three drawings and the spec sheet update together. The derived geometry (bench rectangles, heater position, vent positions, base-frame feet, door swings, seat count, bearing pressure) is computed in `layout()` immediately below the data, and that is the place to change a layout rule rather than a number.

The exterior height in the brief is treated as the height to the high eave. The roof build-up is fixed at 180 mm at the low eave and rises 3 degrees across the width; the floor build-up is 100 mm; the base frame height is whatever remains, which is how the adjustable feet absorb the difference (Perch 194 mm, Lodge 163 mm, Summit 231 mm).

## Checking a change

- `node --check` on the two scripts (copy the first `<script>` block to a `.js` file and the `<script type="module">` block to a `.mjs` file).
- Headless Chrome: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --screenshot=out.png --window-size=1280,8000 file:///path/to/design/index.html`. Add `--use-angle=swiftshader --enable-unsafe-swiftshader` to render the WebGL model without a GPU.

## Caveat

This is a design intent package, not for construction. Structural, electrical and fire-code review by licensed engineers is required for every site. Imperial values are converted from the metric design values; the nominal 8′ × 10′, 10′ × 16′ and 12′ × 24′ footprints in marketing copy are rounded.
