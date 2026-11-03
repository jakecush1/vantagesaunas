# Vantage Sauna Co. marketing site

One self-contained page: `index.html` (inline CSS, inline JS, inline SVG, no raster images, no external scripts). The only external resources are the Fraunces and Inter stylesheets from Google Fonts; the page falls back to system serif and sans-serif faces without them.

## What the page says (Canada, v4)

The copy follows `07-brief/BRIEF.md` (v4, Canada), the source of truth for products, prices, code requirements and go-to-market. Sources for the Canadian facts are in `06-research/` (`canada-codes-and-engineering.md`, `canada-competition-and-costs.md`, `canada-market-research.md`).

- **Market:** Vancouver and Victoria from 2027, Toronto from 2028. Workshop in the Fraser Valley, BC.
- **Audience tabs:** rental towers and business apartments, hotels, condos and strata, developers.
- **Prices, in C$ and before GST/PST/HST:** Perch from C$99,000, Lodge from C$179,000, Summit from C$329,000. Vantage Flex from C$2,150 / C$3,850 / C$6,800 a month over 84 months. Vantage Care C$450 / C$700 / C$1,150 a month. Vantage Access C$300 a month per building. Hotel revenue-share pilot for up to three hotels: 35% of session revenue, C$2,000 a month minimum.
- **Layout (design v3):** both bench tiers run wall to wall along the back wall and face a full-length, privacy-tinted glass front, so every seat has a view. Solid wood side walls carry the door and the heater corner. The Lodge has its shower inside the changing vestibule and weatherproof lockers outside by the entry. The Summit has a 3.4 × 2.8 m changing room with lockers (no nook), and the cold plunge and outdoor shower sit on the terrace. The small plans on the model cards are drawn to scale (10 units = 1 m) from the 3D design page's geometry.
- **Canadian code claims:** 4.8 kPa occupied-roof design load; engineered, flashed anchors in BC (seismic category SC4), ballast only where a Toronto site is SC1/SC2; Canadian-marked (cETLus, cULus or CSA) 208 V heaters to CSA C22.2 No. 164; hard-wired one-hour timer with no override (Ontario); transformer kit for 347/600 V buildings; 850 mm clear door and CSA B651 turning space; CSA A277 factory certification in progress; cold plunge regulated as a pool.
- **Timelines:** 12–20 weeks from contract to first session for Perch and Lodge, 16–26 weeks for Summit.

If the brief changes, update the prices in four places: the model cards, the pricing table, the "Software and service" cards and the FAQ answers.

## Serve it locally

The page links to its sister documents with relative paths (`../02-pitch-deck/`, `../04-design-plans/`), so serve the whole repository, not just this folder. From the repository root:

```sh
python3 -m http.server 8080
```

Then open <http://localhost:8080/03-website/index.html>. Opening `index.html` directly as a file also works, apart from those links if the sister folders are missing.

When served locally there is no `window.claude`, so the "Request a site assessment" form falls back to opening a prefilled `mailto:` link to `hello@vantagesauna.example` (a placeholder address) and shows a thank-you state with a copyable summary of the request.

## Links to the deck and design plans

The hero button "Explore the 3D design plans" and the footer links "Investor deck" and "3D design plans" use relative paths in `href` and carry the published artifact link in `data-live-href`. A small script at the end of the page swaps each `href` for its `data-live-href` when the page runs on claude.ai (when `window.claude` is present). In the repository the relative paths work as they are. To point at different published copies, change the `data-live-href` values.

## Publishing as a Claude artifact

Publish `index.html` with the Artifact tool and pass this `capabilities` object so the form can save submissions:

```json
{
  "db": {
    "rules": [
      { "path": "leads", "read": "admin", "write": "admin" },
      { "path": "leads/{self}", "read": "view", "write": "interact" }
    ]
  },
  "user": {}
}
```

Submissions are written to the `leads` collection, one document per submitter (`leads/<viewer id>`), with the latest request at the top level and earlier requests from the same person in a `history` array. Fields: name, email, company, role, building type, city, building size, roof access and message. Only the artifact owner and Editors can read the collection; each submitter can read only their own entry. Read leads with the `ArtifactData` tool (`list` on collection `leads`).

Only signed-in members of the owner's organisation at Contributor level or above can write to the store. Anyone else who submits the form (outside visitors, signed-out visitors, or anyone whose write is refused) gets the same `mailto:` and copy-summary fallback as the local version.

## Theme

The nav has a light/dark toggle that sets `data-theme` on `<html>` and remembers the choice in `localStorage` (key `vantage-theme`). With no stored choice the page follows the system theme.
