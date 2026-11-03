# Vantage Sauna Co. — Source-of-truth brief (v4, Canada, 2026-11-01)

Every deliverable (business plan, pitch deck, website, 3D design plans, financial model, launch plan) uses the
facts in this file. If a number here conflicts with something elsewhere, this file wins. Sourced research lives in
`06-research/` (Canadian market, codes and engineering, competition and costs; sauna design research). The base
plan below comes from the quarterly cash model in `05-financial-model/` (C$, 2027-2031).

## 1. Brand and company

- Company: **Vantage Sauna Co.** (short: Vantage). Working name; trademark search pending.
- Tagline: **The amenity above everything.**
- One-liner: Vantage designs, factory-builds and installs shared rooftop sauna suites for hotels, rental towers and
  business apartments, and condo buildings, turning unused roof space into the most-loved amenity in the building.
- What we are: a prefab building-products company with a recurring service and software layer. Not a spa operator.
- Voice: warm, precise, Nordic-modern. Confident, no hype. Short sentences.
- Palette: Ember `#C8552B` (accent), Charcoal `#1F1D1B`, Birch `#F4EFE6`, Cedar `#8A5A3C`, Steam `#DCE6E8`,
  Night `#0F1A24` (dark mode). Type: "Fraunces" (display) and "Inter" (body), Google Fonts.
- Founder: Jacob [Last name], Founder & CEO (placeholder surname and bio).
- **Geography: Canada.** Head office and workshop in the Fraser Valley, BC (Langley or Abbotsford, about
  4,000 sq ft at ~C$22/sq ft/yr gross). **Launch Vancouver and Victoria in 2027; add Toronto in 2028** (business
  development from Q2 2028, operations lead 2029, GTA staging bay 2031). Flat-pack kits ship to Toronto by truck.
- Currency **CAD** (C$). Exchange assumption C$1.40 per US$ and C$1.56 per euro (Bank of Canada, Oct 2026).
- Company form: Canadian-controlled private corporation (CCPC), incorporated in BC or federally, head office in
  BC. Keeps the 35% refundable SR&ED credit and small-business tax rate (11% BC, 11.2% ON).
- Timeline: today is 1 Nov 2026. Pre-seed Nov 2026-Mar 2027. **Seed closes by end of Q1 2027.** Engineering,
  certification path and demo Lodge Q1-Q2 2027. **First paid installs Q3 2027.** Year 1 = 2027, Year 5 = 2031.

## 2. Product line (v3 layout + Canadian requirements)

All models: all-electric, factory-built in the Fraser Valley, delivered as an elevator-sized flat-pack panel kit
(default for Perch and Lodge; **panels no larger than 2.0 x 1.1 m**, heaviest piece under 120 kg) or as a craneable
module (Summit, or by request where a staging street exists). **Hot-room layout: both bench tiers run wall to wall
along the back wall and face a full-length, privacy-tinted glass front on the outside wall, so every seat has a
view out; the two short side walls are solid wood and carry the door and the heater corner.** Smart lock and
booking app. Session timers. Seats are bench places at 600 mm; drawn layouts give 5 / 7 / 11 places (7 / 9 / 13 at
550 mm); comfort guideline (3 m3 per person) 4 / 6 / 11.

| Model | Seats | Exterior footprint (W x D x H) | Interior rooms | Heater | Dry weight | Installed price (from, before tax) |
|---|---|---|---|---|---|---|
| **Perch** | 4-6 | 2.4 x 3.0 x 2.9 m | Sauna 2.2 x 2.2 m, ceiling 2.3 m; 0.6 m covered entry porch | 1 x 10.5 kW, 208 V, cETLus/cULus/CSA | ~2,300 kg | **C$99,000** |
| **Lodge** | 8-10 | 3.0 x 4.8 x 3.0 m | Sauna 2.8 x 2.8 m, ceiling 2.4 m; changing vestibule 2.8 x 1.6 m with an indoor shower; weatherproof exterior lockers by the entry | 1 x 18 kW, 208 V, Canadian-marked | ~4,500 kg | **C$179,000** |
| **Summit** | 12-14 | 3.6 x 7.2 x 3.1 m + 3.6 x 3.6 m terrace | Sauna 3.4 x 4.0 m, ceiling 2.4 m; changing room 3.4 x 2.8 m with lockers (no nook); cold plunge 1,200 L (regulated as a pool: dosing, permits); outdoor shower | 2 x 12 kW, 208 V, Canadian-marked | ~8,000 kg + ~1,900 kg plunge filled | **C$329,000** |

Installed price breakdown (what the owner sees on the quote; prices exclude GST/PST/HST):
- Perch C$99,000 = suite hardware 56,000 + engineering, permits and drawings 10,000 + delivery and install 20,500
  + electrical connection 7,500 + commissioning, training and launch 5,000.
- Lodge C$179,000 = 105,500 + 14,000 + 33,500 + 11,500 + 14,500.
- Summit C$329,000 = 201,000 + 21,000 + 58,000 + 22,500 (electrical and water) + 26,500.
- **Site preparation is quoted separately**: BC seismic anchorage and roofing/flashing C$8,000-15,000; 600 V to
  208Y/120 V transformer kit C$10,000-25,000 where the building has only 347/600 V service; structural
  reinforcement where the roof is not rated for occupancy (4.8 kPa); street-use and crane permits for module lifts.
- Add-ons: Lodge cold plunge C$34,500; terrace decking and privacy screens C$12,500-34,000; lighting scene pack
  C$5,000; towel and robe station C$3,000. Average add-ons per contract **C$12,000** (45% margin).
- Product mix 40% Perch / 45% Lodge / 15% Summit. Blended contract value with add-ons **C$181,500**.
- Cost of goods at steady state (materials, factory labour, freight, install crew, electrical sub, engineering and
  permit drawings): Perch C$58,750, Lodge C$103,750, Summit C$187,500 (US cost x 1.25). Hardware gross margin
  **~42%** at steady state; early units cost more (+20% in 2027, +8% in 2028, +3% in 2029). Toronto installs add
  ~C$7,500 freight. Pilot pricing: 15% discount in 2027, 5% in 2028.
- Lead time from signed contract to first session: **12-20 weeks (Perch, Lodge), 16-26 weeks (Summit)**,
  including permits, owner votes and any pool permit. Install on site: 1-2 / 2-3 / 4-6 days.

Canadian requirements built into the product (from `06-research/canada-codes-and-engineering.md`):
- **Base:** in Vancouver and Victoria (seismic category SC4) friction may not resist earthquake forces, so the
  base frame is **bolted to the structure with engineered, flashed anchors** (4-8 posts) and ballast is minimised.
  In Toronto a ballasted, non-penetrating base can still pass where the site is SC1/SC2 and wind checks pass.
  The "zero roof penetrations" claim applies to Toronto only; in BC say "engineered anchors, flashed by a roofer".
- **Loads:** occupied roofs 4.8 kPa (NBC/BCBC/OBC Table 4.1.5.3). Module roof designed for 2.0 kPa snow plus
  drift (Vancouver 1.64 kPa, Toronto 1.12 kPa). Wind to NBC 4.1.7.
- **Electrical:** heaters carry a Canadian mark (cETLus, cULus or CSA) to CSA C22.2 No. 164-18; **208 V-rated**
  heaters; 600 V buildings get the transformer kit; Canadian Electrical Code; **Ontario Rule 62-222: hard-wired
  1-hour timer, no override**, so the app cannot extend a session. Seek a module listing to C22.2 No. 164
  (plus UL 875 for export) and certify the factory to **CSA A277**.
- **Accessibility:** 850 mm clear door (900 mm leaf), 1,500 mm turning space in the Lodge and Summit hot rooms
  (CSA B651), barrier-free route to the roof (building's responsibility; Ontario requires it for rooftop amenity
  spaces). ADA-style transfer section kept as best practice. In BC an indoor shower must be accessible (open item
  for the Lodge vestibule).
- **Fire:** towers of noncombustible construction need a noncombustible wood-look cladding option (or a
  CAN/ULC-S134 test), FRT or tested ceiling boards (flame spread 25 or less), sprinkler-ready module with a
  high-temperature head, horn/strobe tied to the building alarm.
- **Cold plunge:** regulated as a pool in both provinces (BC commercial pool permits; Ontario Class B public cold
  plunge pool): chlorine or bromine dosing with logging, handrail, clock, signs, emergency stop, health notice.

### Construction system (shared spec)
- Base: hot-dip galvanized steel frame on adjustable feet and rubber load-spreading pads/sleepers that carry the
  module to beams and columns. Two variants: **BC (Vancouver, Victoria)** with engineered, flashed structural anchors
  (4-8 posts) and minimal ballast; **Toronto** ballasted with parapet tie-back brackets and no penetrations where the
  site is SC1/SC2 and wind checks pass. Designed for occupied roofs rated 4.8 kPa (NBC/BCBC/OBC).
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
- Heater: commercial electric, 208 V 3-phase, Canadian mark (cETLus, cULus or CSA) to CSA C22.2 No. 164-18; remote
  controller with schedule, hard-wired 1-hour timed cut-off with no override (Ontario Rule 62-222; used everywhere),
  over-temperature cut-off, door sensor. Vantage seeks a module listing to C22.2 No. 164 (plus UL 875 for export).
  Wiring to the Canadian Electrical Code (CSA C22.1; B.C. Electrical Code; Ontario ESC). 600 V buildings get the
  transformer kit. Interior temperature cap 90 C.
- Benches: thermo-aspen, two tiers along the back wall, side wall to side wall, facing the glass; upper bench
  1,150 mm from floor and 700 mm deep (ceiling 1,150-1,250 mm above it, the
  "law of loyly"); lower bench 700 mm high and 500 mm deep; 350 mm step by the door; the far end of the lower
  tier is an ADA-style transfer section (best practice; no Canadian sauna clause) 465 mm high, 1,070 mm long, 560 mm deep, with a lift-out lower-bench section
  beside it that clears the 760 x 1,220 mm transfer space.
- Door and access: 850 mm clear (900 mm leaf), outward-swinging glass door in the near side wall with a
  manifestation strip; 1,500 mm turning space inside the hot room (Lodge, Summit; CSA B651) or on the level landing
  (Perch). Open item: 1,700 mm spaces where BC/OBC treat a changing room as universal.
- Floor: aluminium grating sub-floor with non-slip composite decking, floor drain to roof drain.
- Ventilation: mechanical, 9-12 L/s per person; supply above heater, extract low behind benches.
- Lighting: IP65 LED strips under benches and behind backrests; 2700 K; dimmable scenes.
- Access and safety: Bluetooth/NFC smart lock tied to Vantage Access, occupancy sensor, emergency stop, 90 C cap,
  exterior safety signage, first-aid and drinking-water station.
- Install time on site: Perch 1-2 days, Lodge 2-3 days, Summit 4-6 days. Lead time from signed contract to first
  session: 12-20 weeks (Perch/Lodge), 16-26 weeks (Summit).


## 3. Recurring revenue
- **Vantage Care** service plan: Perch C$450/mo, Lodge C$700/mo, Summit C$1,150/mo. Quarterly inspections, heater
  stones, bench refinishing, 24-hour support, parts, plunge water-quality logging. Attach rate 85%.
- **Vantage Access** software: C$300/mo per building. Booking, smart-lock access, session timers (within the
  1-hour hard cut-off), usage analytics, hotel session pricing. Attach rate 90%. White-label platform at launch.
- Blended recurring per installed building: **C$10,048 per year at 63% gross margin**.

## 4. Commercial models
1. **Purchase** (primary): 50% deposit at contract, 40% at delivery, 10% at commissioning. Care + Access monthly.
   Hotels and short-stay operators recover GST/HST; condos and long-term rental landlords generally cannot, so
   quote them with tax shown. Get a written BC PST ruling before quoting in BC.
2. **Vantage Flex lease** through a Canadian equipment-finance partner (Vantage paid in full at install): from
   C$2,150/mo (Perch), C$3,850/mo (Lodge), C$6,800/mo (Summit), 84 months, Care + Access included.
3. **Hotel revenue-share pilot** (up to 3 lighthouse hotels): C$0 upfront, Vantage takes 35% of session revenue,
   5-year term, C$2,000/mo minimum. Vancouver hotels already sell C$40 sessions (Fairmont Pacific Rim).

## 5. Five-year plan, base case (C$; Year 1 = 2027)

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---|---|---|---|---|
| Installs (Vancouver / Victoria / Toronto) | 5 (4/1/0) | 14 (7/1/6) | 24 (9/2/13) | 34 (11/2/21) | 45 (13/3/29) |
| Installed base, year end | 5 | 19 | 43 | 77 | 122 |
| Hardware revenue (C$M) | 0.77 | 2.41 | 4.36 | 6.17 | 8.17 |
| Recurring revenue (C$M) | 0.01 | 0.12 | 0.30 | 0.59 | 0.99 |
| **Total revenue (C$M)** | **0.78** | **2.53** | **4.66** | **6.76** | **9.16** |
| Gross profit (C$M) | 0.15 | 0.86 | 1.86 | 2.82 | 3.85 |
| Operating expenses (C$M) | 1.05 | 1.18 | 1.70 | 2.13 | 2.53 |
| **EBITDA (C$M)** | **-0.90** | **-0.32** | **+0.15** | **+0.69** | **+1.33** |
| Net income (C$M, after depreciation, interest, IRAP and SR&ED) | -0.93 | -0.25 | +0.08 | +0.63 | +1.26 |
| Capex (C$M) | 0.35 | 0.04 | 0.12 | 0.08 | 0.08 |
| Cash at year end (C$M, with C$2.0M seed and C$0.35M loan) | 1.19 | 0.97 | 1.02 | 1.69 | 2.68 |
| Non-COGS headcount (year end) | 4 | 6 | 8 | 10 | 11 |

122 buildings by 2031 is about 11% of the ~1,140 suitable buildings in the three cities (06-research). Lowest
quarter-end cash C$0.84M in Q2 2029; EBITDA-positive from 2029. **Downside case** (the research's conservative 81
buildings: 5/10/16/23/28 shape): EBITDA about break-even only by 2031; the seed still lasts through 2029, then
the 2029-2030 hires are delayed. Opex lines: non-COGS payroll 0.39 / 0.63 / 0.95 / 1.21 / 1.40; facility 0.066 /
0.088 / 0.150 / 0.176 / 0.236; marketing 0.06 / 0.12 / 0.16 / 0.20 / 0.24; engineering, certification and testing
(non-payroll) 0.26 / 0.08 / 0.09 / 0.10 / 0.11; G&A (insurance, legal, accounting, software, travel) 0.19 / 0.18 /
0.22 / 0.26 / 0.30; platform set-up 0.06 (2027); sales commission 3% of hardware revenue.

## 6. Funding (initial raise)
- **Total to raise: about C$2.15M of equity plus a C$0.35M government-backed loan.**
  - **Pre-seed C$150,000, now to March 2027**: founder, friends and family, Futurpreneur (up to C$75k if the founder
    is 18-39). Pays for incorporation and legal, concept engineering, customer discovery and letters of intent,
    brand and pitch materials (itemised in `08-launch-plan/`).
  - **Seed C$2.0M equity, closing by end of Q1 2027** (range C$1.75-2.25M; SAFE or priced round, valuation not
    stated). BC angels through a registered Eligible Business Corporation get a **30% BC tax credit**. Targets:
    proptech and real-estate investors (Alate Partners, myVentures, Golden Ventures, BC VCCs), strategic real-estate
    owners and hotel groups.
  - **Canada Small Business Financing Program loan C$350,000** (Q2 2027) for the workshop fit-out, tools,
    truck and demo unit (equipment and leaseholds are capped at C$500k); prime + 3%, modelled at 7.45%
    (prime rose to 4.70% on 29 Oct 2026; at 7.70% end-2031 cash is about C$3k lower); 5-year repayment.
  - **Non-dilutive**: NRC IRAP about C$150,000 (2027-2028); SR&ED refunds about C$45-80k a year from 2028.
- Sources and uses, 2027-2028: sources = seed 2.00 + loan 0.35 + gross profit from installs 1.00 + IRAP and SR&ED
  0.23 + customer deposits ahead of builds 0.12 = C$3.70M. Uses = team 1.03 + engineering and certification 0.34 +
  equipment, workshop, truck and demo Lodge 0.39 + G&A 0.37 + marketing and commissions 0.28 + workshop lease
  0.15 + loan interest and principal 0.11 + booking platform 0.06 = C$2.73M, leaving C$0.97M cash at end of 2028.
- No Series A is needed in the base case. An optional growth round in 2029 could speed up Toronto.
- Milestones for the seed: 5 paid installs and 3 lighthouse references by end of 2027; 19 buildings and a Toronto
  pipeline by end of 2028; hardware gross margin 34%+ in 2028 and 40%+ in 2029; zero safety incidents; Canadian
  heater certification and an electrical field-evaluation path in place before the first install.

## 7. Market (sourced; details and links in 06-research/canada-market-research.md)
- Hotels: City of Vancouver ~79 hotels / 13,000 rooms (78.4% occupancy, C$284 ADR in 2025; downtown 80.5% at C$342);
  City of Toronto ~139 hotels / 26,900 rooms (downtown 75.3% at C$350); Victoria ~72 hotels / 5,600 rooms (79.9% occupancy Jan-Aug 2025).
  Pipeline: Toronto 71 projects / 11,665 rooms; Vancouver 45 / 8,562 (Lodging Econometrics Q3 2026).
- Condos: CMHC counts 316,469 condo apartments in Metro Vancouver, 530,838 in the Toronto CMA, 30,768 in Victoria;
  ~1,200 / 1,700 / 60 projects of 100+ units (estimate). BC: a significant change needs a 3/4 vote of votes cast;
  a special levy needs 3/4; reserve-fund spending needs 3/4, or a majority if the depreciation report recommends it.
  Ontario: owners of 66 2/3% of all units must vote yes if the cost exceeds 10% of the budget (board-plus-notice
  below that), and the reserve fund cannot pay for new amenities.
- Rental towers: Toronto registry lists 891 rental buildings of 10+ storeys and 100+ units (710 private); new
  towers are struggling to lease (59% of 2025 GTHA completions unleased at year end; 11.5-14.8% vacancy in new
  Metro Vancouver towers).
- Demand: ~20 circuit-sauna venues in Vancouver (C$24-55 drop-in, C$130-280/month); Othership Toronto C$58 a
  class; Fairmont Pacific Rim sells C$40 sessions; HAVN floating sauna in Victoria.
- Sizing: sourced universe ~4,770 buildings (~C$866M at C$181.5k); **suitable ~1,140 buildings (~C$207M hardware at C$181.5k
  plus ~C$11.5M a year recurring)**; base plan 122 buildings by 2031 (~11%); research's conservative obtainable 81.
- Competition: no Canadian firm sells a turnkey rooftop suite; nearest are residential kits and barrels (C$8-15k)
  and delivered-only commercial cabins (Fritz Tiny Homes from ~C$78k). Hotels' real alternative is the social-sauna
  boom (Othership, Tevah, HAVN).

## 8. Go-to-market
Segments in priority order: (1) purpose-built rental towers and business/serviced apartments (one decision-maker;
lease-up pressure), (2) upscale and lifestyle hotels (revenue-share pilots), (3) condos and strata (slower; BC and
Ontario playbooks with information-session kits and sample resolutions), (4) developers of new rental and hotel
projects (brief architects in 2027 for 2029-2031 deliveries). Channels: direct sales to owners and asset managers,
property-management firms (strata managers), architects and developers, a demo Lodge in the Fraser Valley and a
lighthouse rooftop in Vancouver. Sales cycle: 2-4 months rentals and hotels, 4-9 months condos.

## 9. File map
- `07-brief/BRIEF.md` this file · `08-launch-plan/` funding estimate, startup costs and step-by-step plan
- `01-business-plan/` (Claude Doc export) · `02-pitch-deck/` (viewer, PDF, Slides source) · `03-website/`
- `04-design-plans/` (3D model, drawings, spec) · `05-financial-model/` (Excel model) · `06-research/`
- Live artifacts (private until shared): plan https://claude.ai/artifact/1jg9X32pfVjARyWhqY1Sas, deck
  https://claude.ai/artifact/GXeFrzGzpjB8D6vKRr4g3o, website https://claude.ai/artifact/2Y5n4dxsgFY6mtCPUTFXik,
  design https://claude.ai/artifact/XS6wf21tNce8BkvgW6tzaQ
