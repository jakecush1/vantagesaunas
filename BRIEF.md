# Vantage Sauna Co. — Source-of-truth brief

Every deliverable (business plan, pitch deck, website, 3D design plans, financial model) uses the facts in this file.
If a number here conflicts with something elsewhere, this file wins. Numbers marked (verify) are planning
assumptions awaiting sourced research in `research/`.

## 1. Brand

- Company: **Vantage Sauna Co.** (short: Vantage)
- Tagline: **The amenity above everything.**
- One-liner: Vantage designs, builds, and installs turnkey rooftop sauna suites for apartment buildings, hotels,
  and offices, turning unused roof space into the most-loved amenity in the building.
- What we are: a prefab building-products company with a recurring service and software layer. Not a spa operator.
- Voice: warm, precise, Nordic-modern. Confident, no hype. Short sentences.
- Palette: Ember `#C8552B` (accent), Charcoal `#1F1D1B` (dark), Birch `#F4EFE6` (light background),
  Cedar `#8A5A3C` (wood), Steam `#DCE6E8` (cool neutral), Night `#0F1A24` (dark-mode background).
- Type: display "Fraunces" (serif), body "Inter". Both on Google Fonts.
- Founder: Jacob [Last name], Founder & CEO (placeholder surname; the user is Jacob).
- Geography: United States. Launch market New York City metro. Expansion order: Chicago, Boston, Toronto,
  Denver, Seattle, Minneapolis. Currency USD.
- Timeline: today is 1 Nov 2026. Seed round closes Q1 2027. Pilot installs Q2–Q3 2027. Fiscal year = calendar
  year. Year 1 = 2027, Year 5 = 2031.

## 2. Product line (v2 spec, reconciled to research/sauna-design-research.md on 2026-11-01)

All models: all-electric, factory-built, delivered as an elevator-sized flat-pack panel kit (default for Perch and
Lodge; heaviest piece under 120 kg, panels no larger than 2.3 x 1.2 m) or as a craneable module (optional for
Perch and Lodge, required for Summit), set on a galvanized steel base frame with **zero roof penetrations**
(ballast trays + parapet tie-back per the structural engineer). **Hot-room layout (v3, 2026-11-01): both bench
tiers run wall to wall along the back wall and face a full-length, privacy-tinted glass front on the outside wall,
so every seat has a view out; the two short side walls are solid wood and carry the door and the heater corner.**
Smart lock +
booking app. Session timers. Capacities are bench seats at 600 mm per seat; the comfort guideline of 3 m3 per
person gives 4 / 6 / 11 at full comfort.

| Model | Seats | Exterior footprint (W x D x H) | Interior rooms | Heater | Dry weight (before ballast) | Installed price (from) |
|---|---|---|---|---|---|---|
| **Perch** | 4-6 | 2.4 x 3.0 x 2.9 m (8' x 10' x 9'6") | Sauna 2.2 x 2.2 m, ceiling 2.3 m; 0.6 m covered entry porch | 1 x 10.5 kW, ETL/UL 875 listed | ~2,300 kg (5,100 lb) | **$78,000** |
| **Lodge** | 8-10 | 3.0 x 4.8 x 3.0 m (10' x 16' x 9'10") | Sauna 2.8 x 2.8 m, ceiling 2.4 m; changing vestibule 2.8 x 1.6 m with an indoor shower; weatherproof exterior lockers beside the entry | 1 x 18 kW, ETL/UL 875 listed | ~4,500 kg (9,900 lb) | **$139,000** |
| **Summit** | 12-14 | 3.6 x 7.2 x 3.1 m (12' x 24' x 10'2") + 3.6 x 3.6 m terrace deck | Sauna 3.4 x 4.0 m, ceiling 2.4 m; changing room 3.4 x 2.8 m with lockers (no relaxation nook); cold plunge 1,200 L with 2 HP chiller and ozone/AOP sanitation; outdoor shower | 2 x 12 kW, ETL/UL 875 listed | ~8,000 kg (17,600 lb) module + ~1,900 kg plunge filled | **$249,000** |

Heater sizing follows the Harvia rule of about 1 kW per m3 plus 1.2 m3 of equivalent volume per m2 of glass:
effective volumes are about 16 / 25 / 37 m3 (recomputed for the v3 full-length glass fronts: about 17 / 27 / 44 m3;
Summit's 2 x 12 kW needs confirming). Drawn seat places at 600 mm: 5 / 7 / 11 (7 / 9 / 13 at 550 mm).

Installed price breakdown (what the owner sees on the quote):
- Perch $78,000 = suite hardware $44,000 + engineering, permits and drawings $8,000 + delivery, lift and
  install $16,000 + electrical connection $6,000 + commissioning, training and launch $4,000.
- Lodge $139,000 = $82,000 + $11,000 + $26,000 + $9,000 + $11,000.
- Summit $249,000 = $152,000 + $16,000 + $44,000 + $17,000 (electrical and water) + $20,000.

Add-ons: cold plunge for Lodge ($24,500, 1,200 L, 2 HP chiller), terrace decking + privacy screens
($9,000-$24,000), lighting scene pack ($3,500), towel/robe station ($2,200). Average add-ons per contract:
~$9,000.

Product mix assumption: 40% Perch / 45% Lodge / 15% Summit. Blended hardware average contract value (ACV)
including add-ons: **$140,100** (model) / "$140,000" in prose.

Cost of goods (materials, factory labor, freight, lift, install crew, electrical sub, engineering and permit
drawings): Perch $47k, Lodge $83k, Summit $150k. **Hardware gross margin 40%.** Add-ons 45%.

### Construction system (shared spec)
- Base: hot-dip galvanized steel frame on adjustable feet and rubber load-spreading pads/sleepers that carry the
  module to beams and columns; ballast trays; parapet tie-back brackets; no penetrations. Designed for occupiable
  roofs rated 100 psf (4.8 kPa), the assembly-use load in NYC Building Code Table 1607.1; point loads are reviewed
  by the engineer of record on every site; roofs rated lower (NYC private residential decks are 60 psf) need
  reinforcement, quoted as site preparation.
- Wall panel (outside -> in): 20 mm thermally modified ash/pine cladding (vertical), ventilated 25 mm cavity,
  breathable membrane, 12 mm fiber-cement sheathing (non-combustible), 90 mm mineral-wool insulation
  (non-combustible, Euroclass A1), aluminium-foil vapour barrier rated >= 120 C and <= 0.1 perm, 22 mm ventilated
  batten gap, 15 mm thermo-aspen interior panelling. Total wall ~185 mm.
- Roof: standing-seam steel (non-combustible), 3 deg mono-pitch, integrated gutter and downspout to roof drain.
- Glazing: the whole outside wall of the hot room is a double-glazed tempered insulated glass unit with a
  privacy-tinted reflective (bronze) outer pane and a low-iron inner pane, thermally broken anodized aluminium
  frame. By day bathers see out and the roof sees a dark pane; at night the effect reverses, so the night lighting
  scene keeps the hot room dim (interior blind optional). Side walls are solid wood; the sauna door is a glass leaf
  in the near side wall.
- Heater: commercial electric, ETL/UL 875 listed, 208-240 V 3-phase, remote controller with schedule, 60-minute
  session timer, over-temperature cut-off, door sensor. UL 875 Ed. 10 (2024) covers "a heater unit combined with a
  prefabricated rigid room", so Vantage pursues listing of the whole module. Wiring to NEC Articles 422 and 424 and
  the heater's listing instructions. Interior temperature cap 90 C (194 F).
- Benches: thermo-aspen, two tiers along the back wall, side wall to side wall, facing the glass; upper bench
  1,150 mm from floor and 700 mm deep (ceiling 1,150-1,250 mm above it, the
  "law of loyly"); lower bench 700 mm high and 500 mm deep; 350 mm step by the door; the far end of the lower
  tier is an ADA transfer section 465 mm high, 1,070 mm long, 560 mm deep, with a lift-out lower-bench section
  beside it that clears the 760 x 1,220 mm transfer space.
- Door and access: 813 mm (32 in) clear, outward-swinging glass door in the near side wall; 1,525 mm (60 in)
  turning circle inside the hot room (Lodge, Summit) or on the level landing (Perch).
- Floor: aluminium grating sub-floor with non-slip composite decking, floor drain to roof drain.
- Ventilation: mechanical, 9-12 L/s per person; supply above heater, extract low behind benches.
- Lighting: IP65 LED strips under benches and behind backrests; 2700 K; dimmable scenes.
- Access and safety: Bluetooth/NFC smart lock tied to Vantage Access, occupancy sensor, emergency stop, 90 C cap,
  exterior safety signage, first-aid and drinking-water station.
- Install time on site: Perch 1-2 days, Lodge 2-3 days, Summit 4-6 days. Lead time from signed contract to first
  session: 6-10 weeks (Perch/Lodge), 10-14 weeks (Summit).

## 3. Recurring revenue
- **Vantage Care** service plan: Perch $350/mo, Lodge $550/mo, Summit $900/mo. Quarterly inspections, heater
  stone replacement, bench refinishing, 24-hour support, parts. Gross margin 55%. Attach rate 85%.
- **Vantage Access** software: $249/mo per building. Resident/guest booking, smart-lock access, session timers,
  usage analytics, revenue tools for hotels. Gross margin 80%. Attach rate 90%.
- Blended recurring per installed building: **$8,019 per year at 63.4% gross margin** (after attach rates;
  Care $5,330 + Access $2,689). Model-reconciled 2026-11-01; earlier draft said ~$8,400 at ~65%.

## 4. Commercial models
1. **Purchase** (primary): 50% deposit at contract, 40% at delivery, 10% at commissioning. Care + Access
   billed monthly.
2. **Vantage Flex lease** (via third-party equipment-finance partner; Vantage is paid in full at install):
   from $1,650/mo (Perch), $2,950/mo (Lodge), $5,200/mo (Summit), 84 months, Care + Access included.
   Site prep (structural review, electrical feed) billed separately: $8,000–$25,000.
3. **Hotel revenue-share pilot** (limited to 5 pilot hotels): $0 upfront, Vantage takes 35% of session revenue,
   5-year term, $1,500/mo minimum. Hotels typically price sessions at $35–$60 per guest.

## 5. Five-year plan (Year 1 = 2027)

| | Y1 2027 | Y2 2028 | Y3 2029 | Y4 2030 | Y5 2031 |
|---|---|---|---|---|---|
| Installs (buildings) | 12 | 40 | 95 | 180 | 300 |
| Cumulative installed base (year end) | 12 | 52 | 147 | 327 | 627 |
| Hardware revenue ($M, installs × $140k) | 1.68 | 5.60 | 13.30 | 25.20 | 42.00 |
| Recurring revenue ($M, $8.0k × avg installed base) | 0.05 | 0.26 | 0.80 | 1.90 | 3.82 |
| Total revenue ($M) | 1.73 | 5.86 | 14.11 | 27.12 | 45.85 |
| Gross profit ($M) (40% hw, 63% recurring) | 0.71 | 2.42 | 5.87 | 11.37 | 19.37 |
| Opex ($M) | 2.05 | 3.13 | 5.53 | 9.03 | 13.71 |
| EBITDA ($M) | -1.34 | -0.71 | +0.34 | +2.34 | +5.66 |
| Capex ($M) | 0.60 | 0.40 | 0.70 | 1.00 | 1.50 |
| Non-COGS headcount (year end) | 9 | 18 | 34 | 55 | 85 |

Opex detail ($M): payroll (non-COGS) 0.80 / 1.65 / 3.10 / 5.50 / 8.75; facility lease 0.24 / 0.30 / 0.42 /
0.60 / 0.80; marketing programs 0.30 / 0.50 / 0.90 / 1.40 / 2.00; engineering, certification and R&D
(non-payroll) 0.35 / 0.25 / 0.30 / 0.40 / 0.50; G&A incl. product-liability insurance, legal, software,
travel 0.35 / 0.50 / 0.80 / 1.20 / 1.70.

Average fully loaded cost per non-COGS employee: $115k (Y1) rising ~2%/yr. Direct factory and install labor
sits inside COGS.

The Excel financial model in `financials/vantage-financial-model.xlsx` is the canonical calculation; the table above
was reconciled to it on 2026-11-01 (net income -1.46 / -0.91 / 0.00 / 1.80 / 3.76; closing cash 2.26 / 12.12 /
13.25 / 16.69 / 19.79 incl. $10M Series A in Q4 2028; peak funding need $2.09M in Q3 2028; 7-year LTV $92,078;
LTV:CAC 7.7x to 11.5x).

## 6. Funding
- **Seed ask: $3.5M** (SAFE or priced round; valuation left to negotiation, do not state one).
- Use of funds: product engineering and certification (UL/ETL listing, structural kit, code package, three model
  prototypes) $700k; assembly facility, tooling and first inventory $650k; demo rooftop and three pilot installs
  at cost $500k; sales and marketing $650k; team (ops, install crew ramp) $600k; working capital and reserve
  $400k. Total $3.5M.
- Runway: through Q1 2029. Series A (~$10M) targeted H2 2028 after ~40 installed buildings.
- Milestones to Series A: 40 installed buildings, $5M+ revenue run-rate, 3 metros live, NPS > 60, recurring
  attach > 85%, UL/ETL listing complete, zero safety incidents.

## 7. Market (sourced 2026-11-01; details and links in research/market-research.md)
- US apartment properties with 100+ units: ~56,000 (Census RHFS 2021 via CRS R47332); 81,000 properties have
  50+ units (Census RHFS 2024). Suitable Class A/B+ flat-roof subset: 20,000 (our assumption).
- US hotels: 65,400 properties, 5.79M rooms; luxury + upper-upscale 1.30M rooms, implying ~3,000-5,000
  properties (CoStar/STR via MMCG, Apr 2026). Suitable incl. lifestyle: 5,000 (estimate).
- US office buildings over 100,000 sq ft: 28,000, all classes (EIA CBECS 2018). Class A/trophy subset: 12,000
  (our assumption).
- Sourced universe ~89,000 buildings (~$12.5B at $140k). **Suitable TAM 37,000 buildings = $5.2B hardware +
  ~$300M/yr recurring.** SAM (seven launch metros) 7,500 buildings = $1.05B (assumption, unverified per metro).
  SOM by end of Y5: 627 buildings = $88M cumulative hardware = 1.7% of suitable TAM.
- Deck-safe claims: wellness real estate $876B (2025) growing 15%/yr to $1.8T by 2030, US $254B (GWI May 2026);
  wellness economy $6.8T (GWI Nov 2025); sauna market $954M (2025) to $1.56B (2033), commercial segment 7% CAGR,
  North America 28% (Grand View Research); more than half of renters interested in a hot tub or sauna, rooftop
  space and spa offered by only just over 10% of properties, pools/clubhouses least correlated with rent
  (NMHC/Grace Hill 2024); office roof terrace +5.2% rent premium (JLL via Bisnow, Mar 2024); prime offices +84%
  rent, -4.5 pts vacancy (CBRE via Bisnow); hotel spa revenue $6,061 PAR, $9,847 luxury, 3.4% of revenue (CBRE
  via Spa Business); Bathhouse $35M, Othership $8.5M, Sauna House $9.6M (2025); Perspire 80+ studios.
- Not sourced, label as estimates: sauna-specific rent premium, Class A share, hotel counts by chain scale,
  cold plunge market size, NYC crane and electrical costs, per-metro counts.
- Structural note: NYC residential roof decks are designed to 60 psf live load; Perch and Lodge are engineered
  for 60 psf decks with spreader frames; Summit's filled plunge is placed over primary structure; 100 psf
  amenity decks take any model. Structural reinforcement in NYC "rarely under $15,000" (Block Renovation 2026).

## 8. Go-to-market summary
Segments in priority order: (1) Class A/B+ multifamily owners and asset managers, (2) lifestyle and upscale
hotels, (3) Class A office landlords, (4) others: senior living, student housing, co-living, private clubs.
Channels: direct enterprise sales to owners/asset managers; property-management companies; architects and
developers for new builds; hotel brand wellness teams; a demo rooftop in NYC; pilot program with 3 lighthouse
buildings. Sales cycle assumption 3–6 months; average 1.4 buildings per customer in Y1 growing to 2.5 by Y5
(portfolio roll-outs).

## 9. File map
- `BRIEF.md` this file
- `research/market-research.md`, `research/sauna-design-research.md`
- `website/index.html` marketing site (published as an artifact)
- `design/index.html` interactive 3D design plans + 2D drawings + spec sheet (published as an artifact)
- `financials/vantage-financial-model.xlsx`
- Business plan: Claude Doc. Pitch deck: Claude Slides artifact. URLs in README.md.
