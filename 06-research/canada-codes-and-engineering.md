# Canada: codes, engineering and permitting for Vantage rooftop sauna suites

Prepared 1 Nov 2026 for the Canadian launch: Vancouver (hotels, business/serviced apartments, purpose-built rental towers, strata condos), Victoria, and Toronto (hotels, rental towers, condominium corporations). It checks the current US/NYC spec in `BRIEF.md` section 2 against the codes that apply in British Columbia and Ontario, and lists what has to change.

How to read this file
- Every number carries a source link. All sources were accessed 2026-11-01.
- **[code text read]** = I read the clause in the official code text (BC Building Code 2024 PDF from gov.bc.ca, or Ontario's 2024 Building Code Compendium on ontario.ca). **[page opened]** = I read the web page or PDF itself. **[search excerpt only]** = the fact comes from a search-engine excerpt because the page blocked access (vancouver.ca, NRCan and several others returned HTTP 403). Check excerpt-only facts before they go into a permit set or an investor deck.
- **Estimate** = my own number, with the reasoning given. No figure in this file is invented. Where I could not find a number I say so.
- Plain-English summaries of code clauses are mine. A code consultant and a structural engineer licensed in BC (EGBC) and Ontario (PEO) must confirm all of this for each site.

---

## Bottom line (read this first)

1. **The "zero roof penetrations, ballast only" base does not meet code in Vancouver or Victoria.** BCBC 2024 and the Ontario code (both built on the National Building Code 2020) say that for rooftop components, "friction due to gravity loads shall not be considered to provide resistance to earthquake forces". The only exception is ballasted solar arrays on roofs that are *not normally occupied*. Both cities are in the top seismic category, SC4. My estimate of the design sideways earthquake force on a rooftop module is about **0.8 to 1.1 times its own weight in Vancouver and 1.5 to 1.8 times in Victoria**, at minimum. Adding ballast raises that force, because the force is proportional to weight. The base frame has to be bolted to the building's structure. In Toronto, a ballasted base may still pass seismic checks if the engineer classes the module as equipment and the site is in seismic category SC1 or SC2. Wind still has to be checked.
2. **Heaters must carry a Canadian mark.** Acceptable marks are cETLus, cULus or CSA, to CSA C22.2 No. 164-18 or CSA E60335-2-53. A US-only "ETL" or "UL" mark is not enough. C22.2 No. 164 covers heaters rated **300 V or less**, so in buildings that only have 347/600 V service a step-down transformer is needed. In 120/208 V buildings, Vantage must specify heaters rated for 208 V. A 240 V heater run on 208 V gives about 75% of its rated output.
3. **Ontario's electrical code requires a 1-hour timed cut-off with no override on every sauna heater** (OESC Rule 62-222). This limits how far the Vantage Access app can schedule or extend sessions remotely. Get a written interpretation before launch.
4. **Accessibility rules are stricter than ADA on dimensions and looser on sauna detail.** Doors must give **850 mm clear**, not the 813 mm in the current spec. Universal washrooms and dressing rooms use a **1,700 mm** turning circle. Ontario explicitly requires a barrier-free path to **"rooftop amenity spaces"**. In BC, if a building provides showers (outside a suite), each group of showers must include an accessible one. That affects the Lodge's indoor shower. Neither code has a sauna clause like ADA 612, so keep the ADA transfer bench as best practice.
5. **A cold plunge is a regulated pool in both provinces.** Ontario now defines a "public cold plunge pool" (kept at 15 °C or less and not drained before each user). At condos and apartments with 6 or more units, and at hotels, it is a Class B pool, with 5–10 ppm free chlorine, a handrail, a clock, signs and 14 days' notice to public health before opening. In BC a 1,200 L plunge at a hotel, strata or membership business is a "commercial pool" if it is 61 cm deep or more. It needs a health-authority **construction permit (plans sealed by an engineer or architect) and an annual operating permit**. Saunas themselves are not regulated by public health in either province.
6. **Fire rules for high-rises.** Most towers must be built of noncombustible construction. The thermally modified wood cladding is then allowed only if the building is sprinklered throughout and the wall assembly has passed the CAN/ULC-S134 fire test. Wood ceiling finishes inside need a flame-spread rating of 25 or less. In a sprinklered building the module will probably need a high-temperature sprinkler. A sauna enclosure is not on the list of rooftop enclosures that are left out of the storey count, so in some buildings it could add a storey.
7. **Snow is heavier in Vancouver than in Toronto.** The basic roof snow load is 1.64 kPa at Vancouver City Hall and 1.12 kPa at Toronto City Hall. Occupied roofs take the 4.8 kPa assembly live load in both provinces, the same as the 100 psf NYC figure in the brief.
8. **Timelines are longer than the US 6–10 weeks.** In Ontario the city must decide a complete permit application within 20 business days for Part 3 buildings, or 30 for high-rises. Vancouver's median for commercial renovation permits was 32 days in mid-2024. Strata or condo approval, a pool permit and street-use permits are added on top. My estimate is **12–20 weeks from contract to first session for Perch and Lodge, and 16–26 weeks for Summit**.

---

## 0. Which rules are in force (as of 1 Nov 2026)

| Jurisdiction | Building code | Seismic provisions | Electrical code and authority | Plumbing | Source |
|---|---|---|---|---|---|
| Victoria (and BC outside Vancouver) | **BC Building Code 2024** (in force 8 Mar 2024) | NBC 2020-based seismic required for permits applied for on or after **10 Mar 2025**. Qualifying in-stream projects may use BCBC 2018 seismic until 8 Mar 2027 | **BC Electrical Code = CSA C22.1-24** (CEC 26th ed.), effective **4 Mar 2025**. The City of Victoria issues its own electrical permits. Technical Safety BC issues them elsewhere | BC Plumbing Code 2024, permits from the municipality | [BC Codes 2024 page](https://www2.gov.bc.ca/gov/content/industry/construction-industry/building-codes-standards/bc-codes/2024-bc-codes) [page opened]; [BC bulletin B24-02-R](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/bulletins/2024-code/b24-02-r_seismic_design_delay_period_final.pdf) [page opened]; [TSBC IB-EL 2024-01](https://technicalsafetybc.ca/regulatory-resources/regulatory-notices/information-bulletin-adoption-of-bc-electrical-code-2024-edition) [page opened]; [TSBC jurisdiction](https://www.technicalsafetybc.ca/about-us/jurisdiction) [page opened] |
| Vancouver | **Vancouver Building By-law 2025** (VBBL, based on BCBC 2024), in force **15 Sep 2025** | City guide: new seismic requirements apply to new projects from **15 Sep 2026** | The City of Vancouver issues electrical (and gas) permits itself, not Technical Safety BC | Through the City under VBBL | [City of Vancouver, Guide to 2025 VBBL updates](https://vancouver.ca/files/cov/guide-to-2025-vbbl-updates.pdf) [search excerpt only; 403; **unverified** on fact-check 2026-11-01, still 403]; [bccodes.ca](https://bccodes.ca/vancouver-bylaws.html) [search excerpt only; now redirects to gov.bc.ca, which does not give VBBL dates; **unverified**]; [TSBC jurisdiction](https://www.technicalsafetybc.ca/about-us/jurisdiction) [page opened] |
| Toronto (Ontario) | **Ontario Building Code 2024**, O. Reg. 163/24, in force 1 Jan 2025 (adopts NBC 2020 with Ontario amendments). All applications from 1 Apr 2025 are reviewed under it | Built in (NBC 2020 Part 4) | **Ontario Electrical Safety Code, 29th ed. (2024)**, effective **1 May 2025**. The Electrical Safety Authority (ESA) inspects; a Licensed Electrical Contractor files the notification of work | OBC Part 7, under the building permit | [ontario.ca 2024 OBC](https://www.ontario.ca/page/2024-ontario-building-code) and [OAA transition note](https://oaa.on.ca/whats-on/news-and-insights/news-and-insights-detail/Ontarios-2024-Building-Code-End-of-the-Transition-Period) [search excerpt only]; [ESA OESC page](https://esasafe.com/role/oesc/) [page opened] |

What this means: all three cities use the same NBC 2020 structural, fire and accessibility base, with provincial or city changes. **One product spec can be engineered once for "NBC 2020 + BC + Vancouver + Ontario"** and then adapted per site. Note that I could not open the Vancouver by-law itself (vancouver.ca blocks automated access). Where this file cites BCBC 2024 for Vancouver, the VBBL clause needs checking for a Vancouver-specific change.

---

## 1. Governing code, permits, factory certification, fire rules, timelines

### 1.1 Which code governs a factory-built rooftop sauna on an existing building

- **It is building work on an existing Part 3 building.** Hotels, rental towers and condo towers are almost always "Part 3" buildings: over 600 m² footprint, over 3 storeys, or containing assembly use. The new enclosure must meet the current code (BCBC 2024, VBBL 2025 or OBC 2024). Existing parts of the building generally only need upgrading where the new work triggers it.
  - Ontario puts this in Part 11 (Renovation). New work "shall comply with all other Parts", and the existing building's "performance level" must not be reduced. If a change of use raises the live load and the existing roof framing "is not adequate", remedial work is required, or the area must be load-restricted and signed. [OBC 2024 Part 11, 11.3.1.2, 11.4.2.1, 11.4.3.2](https://www.ontario.ca/document/2024-building-code-compendium/part-11-renovation) [code text read]
  - Ontario's Part 11 hazard-index table lists **"Public Saunas" under Group D** (business and personal services). A hotel sauna sold to outside guests could be read as a Group D use, which matters for change-of-use permits. [OBC Part 11, Table 11.2.1.1.-J](https://www.ontario.ca/document/2024-building-code-compendium/part-11-renovation) [code text read]
  - In BC, accessibility upgrades for alterations apply "where providing such access would be practical" (3.8.4.5). Vancouver has its own Part 11 for upgrades to existing buildings, which I could not read. [BCBC 2024 3.8.4](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]; [VBBL Part 11 draft change 24-0030](https://vancouver.ca/files/cov/ccr-24-0030-existing-buildings.pdf) [search excerpt only]
- **Zoning is a separate gate.** Vancouver's Zoning and Development By-law lets the Director of Planning approve "common roof-top amenity structures … that do not exceed a height of **3.6 m**" above the height limit. That is discretionary, so expect a development permit step. Perch, Lodge and Summit are 2.9–3.1 m tall, which fits. [Vancouver Zoning By-law s.10](https://bylaws.vancouver.ca/zoning/zoning-by-law-section-10.pdf) [search excerpt only; **unverified** on fact-check 2026-11-01, 403]. Toronto's zoning by-law 569-2013 lets unenclosed rooftop amenity structures exceed the height limit (3.0 m in commercial zones). Recent site-specific by-laws allow 4–5 m for trellises and wind screens. **An enclosed sauna is not clearly covered and may need a minor variance.** [Toronto zoning amendments](https://www.toronto.ca/zoning/bylaw_amendments/ZBL_NewProvision_Chapter40.htm), [Bill 645 (2026)](https://www.toronto.ca/legdocs/bills/2026/bill0645.pdf) [search excerpt only]

### 1.2 Permits needed, by city

| Permit or approval | Vancouver | Victoria | Toronto |
|---|---|---|---|
| Owner approval | Strata: a "significant change" to common property needs a **3/4 vote** at a general meeting (Strata Property Act s.71). Hotels and rentals: owner sign-off | Same as Vancouver | Condo: a "substantial" change (estimated cost over 10% of the annual budgeted common expenses, or the board elects to treat it as substantial) needs **owners of at least 66⅔% of all units** to vote in favour at a meeting called for it, not 2/3 of the votes cast (Condominium Act s.97(4)–(6)). Smaller changes (over 1% of the budget or $1,000) need notice to owners and a 30-day window to requisition a meeting (s.97(3)). *Corrected on fact-check 2026-11-01.* |
| Zoning or development | Development permit likely, because the rooftop amenity structure relaxation is discretionary | City of Victoria zoning check (not researched) | Zoning review; minor variance (Committee of Adjustment) if the enclosure exceeds the height limit |
| Building permit | City of Vancouver under VBBL 2025, with structural letters of assurance (BC practice; EGBC engineer) | City of Victoria under BCBC 2024 | Toronto Building under OBC 2024, Large/Complex stream |
| Electrical | **City of Vancouver** electrical permit (the City runs the BC Safety Standards Act locally) | **City of Victoria** electrical permit | **ESA notification of work** filed by a Licensed Electrical Contractor. ESA's 2025 sauna notice says the owner also needs a building permit |
| Plumbing (Lodge shower, Summit plunge, drains) | City plumbing permit | City plumbing permit | Part of the building permit (OBC Part 7) |
| Cold plunge (Summit or Lodge add-on) | Vancouver Coastal Health: **construction permit + operating permit** under the BC Pool Regulation | Island Health: same | Toronto Public Health: Reg. 565 Class B pool, **notify 14 days before opening** |
| Street use or crane | Street use permit from the City Engineer to occupy a street *or the air space above it* | Street Occupancy Permit | Street Occupation Permit (hoisting by mobile crane or boom truck) |

Sources: [Strata Property Act s.71](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/98043_05) [statute text read, fact-check 2026-11-01]; [BC strata s.71 summary, BCLI](https://www.bcli.org/?p=13742) [search excerpt only]; [Ontario Condominium Act, 1998, s.97](https://www.ontario.ca/laws/statute/98c19) [statute text read, fact-check 2026-11-01] and [FirstService summary](https://www.fsresidential.com/ontario/news-events/articles/condo-common-elements/) [search excerpt only]; [TSBC jurisdiction](https://www.technicalsafetybc.ca/about-us/jurisdiction) [page opened]; [ESA Flash 25-20-FL, May 2025](https://esasafe.com/assets/files/esasafe/pdf/Electrical_Safety_Products/Flash_Notices/25-20-FL.pdf) [page opened]; [BC Pool Regulation](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/296_2010) [page opened]; [Halton Pool and Spa Operator Guide, Sep 2025](https://www.halton.ca/Repository/Pool-Owner-Operator-Information-Package) [page opened]; street use sources in section 5.

### 1.3 Does a factory-built unit need CSA A277 certification?

**It is not mandatory in either province. In practice it is worth getting.**
- CSA A277 ("Procedure for certification of prefabricated buildings, modules, and panels") is a factory quality and inspection procedure, "not a building code". BCBC 2024 says the code "applies the same requirements to site-built and factory-constructed buildings". If a unit carries an accredited agency's A277 label, "the accepting authority will have some assurance that the concealed components do not require re-inspection on site". Without the label, inspectors can ask to open up panels or inspect in the factory. [BCBC 2024 Note A-1.1.1.1.(3)](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]
- Ontario goes further. "A manufactured building or a manufactured part of a building within the scope of Part 3 is **deemed to comply** with this Code if it is certified in accordance with CSA A277." Site installation is still inspected. [OBC 2024 Division C 1.12.1.1](https://www.ontario.ca/document/2024-building-code-compendium/part-1-general-0) [code text read]. A Toronto staff report notes that inspectors no longer have to visit the factory for A277-certified modules. [Toronto staff report, 2025](https://www.toronto.ca/legdocs/mmis/2025/ph/bgrd/backgroundfile-253704.pdf) [search excerpt only]. The OBC references the 2016 edition (CSA A277-16). [OBC Div B Table 1.3.1.2](https://www.ontario.ca/document/2024-building-code-compendium/part-1-general) [code text read]
- A277 covers the building side only. The **electrical** side (heater plus wiring plus room) needs its own certification or a field evaluation (section 3).
- Recommendation: certify the Vantage factory and the panel kit to A277 through an SCC-accredited body such as QAI, Intertek or CSA, scoped to NBC 2020, BCBC 2024, VBBL 2025 and OBC 2024. Cost was not found; budget **CAD 20–50k first year plus audits** (estimate, based on the scope of a factory audit program; get quotes).

### 1.4 Fire and combustibility rules for rooftop structures

1. **The enclosure may count as a storey.** Only rooftop enclosures for elevator machinery, a service room, an access/egress stair or an elevator lobby are excluded "in calculating the building height". [BCBC 2024 3.2.1.1.(1)](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]. Ontario's list is shorter still: elevator machinery, a stairway, or a service room "used for no purpose other than for service to the building". [OBC 3.2.1.1.(1)](https://www.ontario.ca/document/2024-building-code-compendium/part-3-fire-protection-occupant-safety-and-accessibility) [code text read]. A sauna is not on either list. On a 6-storey wood-frame rental building (common in Vancouver and Victoria) a sauna could make it "7 storeys" and break the combustible-construction limits. **Get a code consultant's opinion or an alternative solution before selling into 4–6 storey wood buildings.**
2. **Noncombustible host buildings (most towers).** A part of a building required to be noncombustible must use noncombustible materials, except for the listed allowances. [BCBC 2024 3.1.5.1](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]
   - **Exterior wood cladding** is allowed only if the building is 3 storeys or less *or* sprinklered throughout, **and** the wall assembly passes **CAN/ULC-S134**: flaming no more than 5 m above the opening, and heat flux no more than 35 kW/m² at 3.5 m. Fire-retardant-treated wood must be tested after accelerated weathering. [BCBC 3.1.5.5](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]. The current thermally modified ash cladding has no S134 test, so on towers use noncombustible cladding (aluminium or steel profiles, fibre cement) or fund an S134 test.
   - **Interior finishes**: wall finishes up to 25 mm thick with a flame-spread rating of 150 or less are allowed. Ceiling finishes up to 25 mm thick need a flame-spread rating of **25 or less**, with up to 10% of the ceiling allowed at 150, unless they are fire-retardant-treated wood. [BCBC 3.1.5.12](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]. The 15 mm thermo-aspen ceiling almost certainly does not reach 25 (estimate: untreated softwood and hardwood boards usually test well above 25). Options: CAN/ULC-S102 testing of the actual boards, a fire-retardant-treated ceiling (an odour and off-gassing question in a 90 °C room), or an alternative solution.
   - Mineral wool and fibre-cement sheathing are already noncombustible. Foil vapour barriers count as minor components. [BCBC 3.1.5.2](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]
3. **Sprinklers.** NBC-based codes call up NFPA 13 for sprinklered buildings. NFPA 13 "generally requires sprinklering of any concealed spaces of combustible construction or where large amounts of combustibles are present". [BCBC Note A-3.1.11.5.(3)](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]. Fire protection engineers report that saunas in sprinklered buildings are sprinklered, typically with **286 °F (141 °C) heads**. [MeyerFire forum, Mar 2024](https://www.meyerfire.com/daily/saunas-considered-bathrooms-for-sprinklers) [page opened]. NFPA 13 classes 250–300 °F heads as "High" (225 °F maximum ceiling temperature) and 325–375 °F as "Extra High" (300 °F ceiling). [NFPA 13 Table, via NFPA first revision report](https://docinfofiles.nfpa.org/files/AboutTheCodes/13/13_A2018_AUT_PRI_FRReport.pdf) [search excerpt only]. Design change: a sprinkler-ready module (dry-pendent high-temperature head in the hot room, standard head in the vestibule, a stub for connection to the building's system, freeze protection for Toronto's −20 °C design temperature).
4. **People on the roof trigger exit rules.** "Means of egress shall be provided from every roof which is intended for occupancy". The exit at roof level must be "designed in conformance with the requirements for exits", which in practice means an exit stair, not a hatch. **Two** exits are required if the roof's occupant load is **more than 60**. A rooftop enclosure that is not itself an exit needs an access to exit leading to an exit at roof level or on the storey below. [BCBC 3.3.1.3.(3)–(9)](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]
5. **Fire alarm** signals must be "clearly audible … throughout any occupancy on a roof". [BCBC 3.2.4.18](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]. This rules out a module that blocks alarm sound (add a horn and strobe inside, tied to the building system).
6. **Guards** of at least **1,070 mm** are required "around any roof to which access is provided for purposes other than maintenance". They must be non-climbable between 140 and 900 mm where the drop is more than one storey. [BCBC 3.3.1.18](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]. Many existing parapets are lower, so this is site preparation.
7. **Sauna fire history in Ontario.** The Fire Marshal and ESA recorded **3 sauna-fire deaths in 10 years**. They name the main causes as combustibles left in the room, missing or bypassed high-limit switches and thermostats, unapproved replacement parts, and heaters too close to combustibles. [ESA Flash 25-20-FL](https://esasafe.com/assets/files/esasafe/pdf/Electrical_Safety_Products/Flash_Notices/25-20-FL.pdf) [page opened]. This supports Vantage Care's tamper-evident controls and parts-only-from-Vantage policy.

### 1.5 Typical permit timelines

| City | What the sources say | Source |
|---|---|---|
| Toronto | The Chief Building Official must issue or refuse a *complete* application within **20 business days** for Part 3 buildings, or **30** for buildings where Subsection 3.2.6 applies (high buildings). Toronto routes Part 3 work to its Large/Complex stream | [OBC Div C 1.3.1.3 and Table 1.3.1.3](https://www.ontario.ca/document/2024-building-code-compendium/part-1-general-0) [code text read]; [Toronto review streams](https://www.toronto.ca/services-payments/building-construction/apply-for-a-building-permit/building-permit-review-streams) [page opened] |
| Toronto (performance) | A City audit found **17 of 27** complete applications (63%) missed the legislated time frames | [Toronto audit report, 2024](https://www.toronto.ca/legdocs/mmis/2024/au/bgrd/backgroundfile-243032.pdf) [PDF opened, fact-check 2026-11-01] |
| Vancouver | Commercial renovation permits: **median 32 days** in mid-2024, down from 56 days in 2022. Permits were issued "40% faster in 2025 vs 2022" | [City news, Jul 2024](https://vancouver.ca/news-calendar/residents-and-businesses-can-obtain-permits-easier-july-2024.aspx); [City fact sheet, Jun 2026](https://vancouver.ca/files/cov/fact-sheet-permitting-improvements-june%202026.pdf) [search excerpt only; **unverified** on fact-check 2026-11-01, vancouver.ca returns 403] |
| Victoria | No published processing time found. The City offers pre-application meetings | [Victoria building permits](https://www.victoria.ca/building-business/permits-development-construction/building-renovating/building-permits) [search excerpt only] |

**Estimate, contract to first session in Canada:**
- Engineering and drawings: 2–4 weeks.
- Strata or condo approval: 2–8 weeks, depending on meeting notice periods.
- Building permit: 4–8 weeks (Toronto 20–30 business days if complete; Vancouver about 5–7 weeks at the 2024–25 medians).
- Electrical permit, run in parallel.
- Pool permit for the plunge: 2–6 weeks.
- Crane street use: 1–2 weeks.
- Factory build, run in parallel: 4–6 weeks.

Total: **12–20 weeks for Perch and Lodge, 16–26 weeks for Summit**, against 6–10 and 10–14 weeks in the brief. The extra time comes from owner votes and the plunge permit, not fabrication.

---

## 2. Loads

### 2.1 Roof live loads (identical text in BCBC 2024 and OBC 2024, both NBC 2020)

| Use | Specified live load | Source |
|---|---|---|
| Ordinary roof | **1.0 kPa** (about 21 psf), or snow if higher | [OBC Table 4.1.5.3](https://www.ontario.ca/document/2024-building-code-compendium/part-4-structural-design) [code text read]; [BCBC Table 4.1.5.3](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read] |
| Exterior areas accessible to pedestrians (roof decks, amenity roofs) | **Not less than the greater of the assembly load (4.8 kPa) or the snow and rain load** | 4.1.5.5.(3), same sources [code text read] |
| Assembly areas (no fixed seats), exits, lobbies, exterior balconies | **4.8 kPa** (100 psf) | Table 4.1.5.3 [code text read] |
| Recreation areas that cannot be used for assembly | 3.6 kPa | Table 4.1.5.3 [code text read] |
| Equipment areas and service rooms | 3.6 kPa | Table 4.1.5.3 [code text read] |
| Residential areas | 1.9 kPa | Table 4.1.5.3 [code text read] |
| Concentrated load on roof surfaces | 1.3 kN over 200 × 200 mm | Table 4.1.5.9 [code text read] |

Plain English: the brief's "designed for occupiable roofs rated 4.8 kPa" carries over directly. The Canadian sticking point is that **an existing ordinary roof is designed for 1.0 kPa or snow**, which is far below what a sauna and its users need. Ontario Part 11 requires remedial work if the roof framing "is not adequate" for the new use (11.4.2.1, 11.4.3.2 [code text read]).

Module bearing pressure (my arithmetic from the brief's weights and footprints):
- Perch: 2,300 kg on 7.2 m² ≈ **3.1 kPa** dry.
- Lodge: 4,500 kg on 14.4 m² ≈ **3.1 kPa**.
- Summit: 8,000 kg on 25.9 m² ≈ **3.0 kPa**, plus a 1,900 kg plunge.

That is before ballast, occupants (roughly 0.6 kPa for 10 people at 90 kg over the Lodge hot room) and snow on the module roof. Even a 4.8 kPa amenity roof cannot take this as a uniform load everywhere. Spreader frames to beams or columns remain essential, as the brief says.

### 2.2 Snow (1-in-50-year ground snow Ss and rain Sr, from the code climate tables)

| Location | Ss (kPa) | Sr (kPa) | Basic roof snow on a small flat roof, S = 1.0 × [Ss × 0.8 + Sr] (kPa) | Source |
|---|---|---|---|---|
| Vancouver (City Hall) | **1.8** | **0.2** | **1.64** | [BCBC 2024 Table C-2](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read] |
| Vancouver (Granville St & 41st Ave) | 1.9 | 0.3 | 1.82 | same |
| Victoria (Table C-2 "Victoria", 10 m elevation) | **1.1** | **0.2** | **1.08** | same |
| Victoria (Gonzales Hts; this is the row the City's bulletin uses) | 1.5 | 0.3 | 1.50 | same; [City of Victoria bulletin, 11 Mar 2025](https://www.victoria.ca/media/file/climatic-and-seismic-data-2025-03-11) [page opened] |
| Toronto (City Hall) | **0.9** | **0.4** | **1.12** | [OBC 2024 SB-1 Table 2](https://www.ontario.ca/document/2024-building-code-compendium/sb-1-climatic-and-seismic-data) [code text read] |

How the last column was worked out: the code formula is S = Is[Ss(Cb·Cw·Cs·Ca) + Sr] [code text read, 4.1.6.2]. I used Is = 1.0 (normal importance), Cb = 0.8 (small roof), Cw = 1.0, Cs = 1.0 (3° slope) and Ca = 1.0 (no drift). These are code defaults, but the engineer sets the final values.
- **Drift matters.** The code adds accumulation "on areas adjacent to roof projections, such as penthouses, large chimneys and equipment" (4.1.6.7). A 3 m-tall sauna is such a projection. The host roof beside it gets a drift load, and drains must not sit in the drift zone. Snow sliding off the mono-pitch roof (4.1.6.11) must also be checked. [OBC 4.1.6.2–4.1.6.11](https://www.ontario.ca/document/2024-building-code-compendium/part-4-structural-design) [code text read]
- Design the module roof for at least **2.0 kPa plus drift**, so that one roof design covers all three cities (estimate: rounds up the 1.82 kPa Vancouver Granville case).

### 2.3 Wind

| Location | Hourly wind pressure q, 1-in-10 / 1-in-50 (kPa) | Source |
|---|---|---|
| Vancouver (City Hall) | 0.34 / **0.45** | [BCBC 2024 Table C-2](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read] |
| Victoria | 0.46 / **0.57** | same; [City bulletin](https://www.victoria.ca/media/file/climatic-and-seismic-data-2025-03-11) [page opened] |
| Toronto (City Hall) | 0.34 / **0.44** | [OBC SB-1 Table 2](https://www.ontario.ca/document/2024-building-code-compendium/sb-1-climatic-and-seismic-data) [code text read] |

- Method: p = Iw·q·Ce·Ct·Cg·Cp with the 1-in-50 q. The exposure factor is Ce = (h/10)^0.2 (min 0.9) for open terrain and 0.7(h/12)^0.3 (min 0.7) for rough or urban terrain. Cg is 2.0 for the structure as a whole. Computational fluid dynamics "shall not be used". [OBC 4.1.7.1, 4.1.7.3](https://www.ontario.ca/document/2024-building-code-compendium/part-4-structural-design) [code text read]. This replaces the ASCE 7 GCr method in the US research.
- **Estimate, Lodge on a 60 m roof**: long face 4.8 × 3.0 m = 14.4 m². I assumed a net CgCp of about 2.6 (Cg 2.0 × 1.3 combined windward and leeward Cp) for a small box; the engineer will refine this.
  - Vancouver: p ≈ 1.3 kPa (urban) to 1.7 kPa (waterfront), so about **19–24 kN** sideways.
  - Victoria: about 1.7–2.1 kPa, **24–31 kN**.
  - Toronto: about 1.3–1.6 kPa, **19–24 kN**.
  - Against the Lodge's 44 kN dry weight and a pad-on-membrane friction coefficient of perhaps 0.3–0.5 (estimate), friction gives 13–22 kN. **Even where seismic rules allow friction (Toronto), wind on tall or exposed buildings will often need tie-downs or ballast.**

### 2.4 Seismic: the decisive Canadian issue

**Hazard values (2% in 50 years, NBC 2020 model)**

BCBC 2024 Table C-3 lists Smax for Part 9 design, defined as the larger of ⅔·S(0.2) and S(0.5). So the design value S(0.2) used for rooftop components is **at least Smax and at most 1.5 × Smax**. [BCBC Appendix C, Smax procedure](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]

| Location | Smax, site class C (firm ground) | Smax, site class D (stiff soil) | Smax, unknown site | Source |
|---|---|---|---|---|
| Vancouver (City Hall) | 0.884 | 1.18 | 1.24 | BCBC 2024 Table C-3 [code text read] |
| Victoria | 1.68 | 2.00 | 2.01 | BCBC 2024 Table C-3 [code text read]; [City bulletin](https://www.victoria.ca/media/file/climatic-and-seismic-data-2025-03-11) [page opened] |
| Toronto (City Hall) | Sa(0.2) = **0.249** (Part 9 table, carried over from the 2012 code; Part 4 values come from the NRCan tool, and Ontario's hazard "has increased") | n/a | n/a | [OBC SB-1 Table 3 and text](https://www.ontario.ca/document/2024-building-code-compendium/sb-1-climatic-and-seismic-data) [code text read] |

The BC bulletin explains why Victoria's hazard jumped: new knowledge of the **Leech River fault** near Victoria, more frequent Cascadia great earthquakes, and new ground-motion models. [BC bulletin B24-02-R](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/bulletins/2024-code/b24-02-r_seismic_design_delay_period_final.pdf) [page opened]

**Seismic Category** (Table 4.1.8.5.-B) [code text read]:

| Category | IE·S(0.2) | IE·S(1.0) |
|---|---|---|
| SC1 | below 0.2 | below 0.1 |
| SC2 | 0.2 to below 0.35 | 0.1 to below 0.2 |
| SC3 | 0.35 to 0.75 | 0.2 to 0.3 |
| SC4 | above 0.75 | above 0.3 |

The building takes the more severe of the two categories (Note 1 to the table). *Corrected on fact-check 2026-11-01: the IE·S(1.0) column was missing. [BCBC 2024 Table 4.1.8.5.-B](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) and [OBC 2024 Table 4.1.8.5.-B](https://www.ontario.ca/document/2024-building-code-compendium/part-4-structural-design) [code text read]*

- Vancouver (S(0.2) at least 0.884 on firm ground) and Victoria (at least 1.68) are **SC4**.
- Toronto is probably **SC2** on firm ground (about 0.25). This is my estimate. It may be SC3 on soft waterfront or fill sites, because the 2024 hazard is higher than the 2012-era table value. Run the NRCan tool for each Toronto site. The long-period value IE·S(1.0) also counts, and on soft sites it can set the category, so get both values.

**What NBC 2020 / BCBC 2024 / OBC 2024 Article 4.1.8.18 requires** [code text read in both codes]:
- Rooftop "machinery, fixtures, equipment and tanks (including contents)" (Category 11) and "penthouses" (Category 5) are designed for a lateral force **Vp = 0.3 · S(0.2) · IE · Sp · Wp**.
  - Sp = Cp·Ar·Ax/Rp, between 0.7 and 4.0.
  - At roof level the height factor is **Ax = 1 + 2·hx/hn = 3.0**.
  - Equipment is assumed "flexible or flexibly connected" unless shown to have a period of 0.06 s or less. That gives Cp 1.0, Ar 2.5, Rp 2.5, so **Sp = 3.0**. If proven rigid: Ar 1.0, Rp 1.25, so Sp = 2.4.
- **Connections "shall be designed to support the component … for gravity loads … and … friction due to gravity loads shall not be considered to provide resistance to earthquake forces"** (4.1.8.18.(7)(a) in both BCBC and OBC; *OBC sentence number corrected on fact-check 2026-11-01*).
- The **only** exception is a ballasted array of interconnected solar panels where IE·S(0.2) is 1.0 or less. It applies only if "the roof is not normally occupied" and the parapet, height, slope, clearance and tested-friction conditions are all met (4.1.8.18.(17)–(18)). **An occupied amenity roof can never use it.**
- Post-installed anchors in concrete must be pre-qualified for seismic use by cyclic testing (CSA A23.3; ACI 355.2 or 355.4). Shallow anchors use Rp = 1.5. Adhesive or power-actuated (non-ductile) connections use Rp = 1.0, and power-actuated fasteners are not allowed for cyclic tension.
- For SC1 and SC2 buildings, Sentence (1) "need not apply to Categories **6 through 22**" (equipment, components). It *does* still apply to Category 5 (penthouses). In Toronto, how the engineer classes the module decides whether it needs seismic restraint.
- Glass: the glazing must not fall out at 1.25 × the design drift (or 13 mm). This does not apply in SC1/SC2, or to fully tempered *monolithic* glass in non-post-disaster buildings within 3 m of a walking surface (4.1.8.18.(14)–(15)). The full-length tempered IGU front needs its frame clearance checked in BC.
- Guidance for nonstructural seismic restraint is in **CSA S832**. [BCBC Note A-Table 4.1.8.18](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]

**Estimate: design lateral earthquake force on each module (flexible assumption, IE = 1.0, Ax = 3.0, Wp = dry weight, S(0.2) taken = Smax, which is the low end of the possible range)**

| Site | Vp / Wp | Perch (22.6 kN) | Lodge (44.1 kN) | Summit module (78.5 kN) | Summit plunge, filled (18.6 kN) |
|---|---|---|---|---|---|
| Vancouver, site class C | ≥ 0.80 | ≥ 18 kN | ≥ 35 kN | ≥ 63 kN | ≥ 15 kN |
| Vancouver, site class D | ≥ 1.06 | ≥ 24 kN | ≥ 47 kN | ≥ 83 kN | ≥ 20 kN |
| Victoria, site class C | ≥ 1.51 | ≥ 34 kN | ≥ 67 kN | ≥ 119 kN | ≥ 28 kN |
| Victoria, site class D | ≥ 1.80 | ≥ 41 kN | ≥ 79 kN | ≥ 141 kN | ≥ 34 kN |
| Toronto (0.249) | 0.22 | 5 kN | 10 kN | 18 kN | 4 kN |

Arithmetic: Vp/Wp = 0.3 × S(0.2) × 1.0 × 3.0. Upper values (S(0.2) = 1.5 × Smax) are 50% higher. If the module is proven rigid, multiply by 0.8. Ballast that rides with the module adds to Wp and so **adds** to Vp.

**Is a ballast-only, non-penetrating base acceptable?**
- **Vancouver and Victoria: no.** The code bars counting friction, and the solar exception excludes occupied roofs. The base frame must be positively connected to structure that can take forces about equal to (Vancouver) or about twice (Victoria) the module's weight.
- **Toronto: possibly**, if the engineer classes the module as Category 11 or 18–21 equipment and the site is SC1 or SC2. Wind and overturning still have to be resisted, by ballast, tie-backs or both. If the building official treats it as a Category 5 "penthouse", Vp of about 0.22 × weight applies and friction cannot be counted.

### 2.5 What this means for the steel base frame

1. **Make two base variants:**
   - **"BC seismic base"** (Vancouver, Victoria, any SC3/SC4 site): 4–8 structural posts or pedestals per module, bolted to the slab or beams with seismically pre-qualified anchors. Each post gets a factory-flashed curb compatible with common membranes (SBS, PVC, TPO). Base members are sized for Vp at the upper bound (up to about 2.7 × weight in Victoria on soft soil), plus overturning.
   - **"Ontario ballast base"** (SC1/SC2, engineer agrees it is Category 11 or 18–21): the current ballast trays plus parapet tie-back, checked for wind sliding and uplift.
2. **Drop "zero roof penetrations" from BC marketing.** Say "a small number of engineered, flashed structural anchors, coordinated with the roofer to keep the membrane warranty".
3. **Parapet tie-backs count as seismic connections in BC.** They must be designed for the full share of Vp. The parapet itself must be checked; existing parapets are rarely designed for 35–140 kN point loads.
4. **Ballast is the enemy in BC.** Every kilogram of ballast moving with the module adds earthquake load. Use it only where it serves wind uplift and the anchors can take the extra seismic mass.
5. **Plunge tank:** anchor the tank as a "tank including contents" (Category 11) with the water mass included. Check sloshing, and the 10%-of-floor-mass rule in 4.1.8.18.(5).
6. **Glazing:** specify frame clearances so the IGU does not fall out at the code drift, or use a laminated inner lite, on BC jobs.
7. **Drift accommodation:** pipe, drain and conduit connections from the building to the module need flexible joints sized for building drift.

---

## 3. Electrical

### 3.1 Codes, inspectors and approval of equipment

- BC: CSA C22.1-24 is the BC Electrical Code from 4 Mar 2025 [TSBC IB-EL 2024-01](https://technicalsafetybc.ca/regulatory-resources/regulatory-notices/information-bulletin-adoption-of-bc-electrical-code-2024-edition) [page opened]. The **City of Vancouver** and **City of Victoria** issue their own electrical permits; Technical Safety BC "typically does not issue permits" there. [TSBC jurisdiction](https://www.technicalsafetybc.ca/about-us/jurisdiction) [page opened]
- Ontario: OESC 29th edition (2024), effective 1 May 2025. [ESA](https://esasafe.com/role/oesc/) [page opened]. A Licensed Electrical Contractor files the ESA notification for the sauna's electrical connections. [ESA Flash 25-20-FL](https://esasafe.com/assets/files/esasafe/pdf/Electrical_Safety_Products/Flash_Notices/25-20-FL.pdf) [page opened]
- Approval of equipment: the CEC defines "approved" as certified by a body accredited by the Standards Council of Canada. BC requires a certification mark or a Technical Safety BC (or SPE-1000 field) approval label (Electrical Safety Regulation s.21). [UL Canada, Acceptance of Electrical Products in Canada](https://canada.ul.com/wp-content/uploads/sites/11/2018/05/Acceptance-of-Electrical-Products-in-Canada-1.pdf) [page opened]; [TSBC approved marks bulletin B-E3 071019 3, rev. 13, 22 May 2024](https://www.technicalsafetybc.ca/regulatory-resources/regulatory-notices/approved-certification-marks-electrical-products) [page opened]. Ontario's O. Reg. 438/07 requires every electrical product to be approved. ESA lists the recognized marks, including CSA, UL/ULC, Intertek, QPS, TÜV, SGS, Nemko, and SPE-1000 field evaluation marks. [ESA recognized marks](https://esasafe.com/electrical-products/recognized-certification-marks/) [page opened]

### 3.2 Sauna-specific installation rules

ESA quotes these OESC rules for saunas [ESA Flash 25-20-FL](https://esasafe.com/assets/files/esasafe/pdf/Electrical_Safety_Products/Flash_Notices/25-20-FL.pdf) [page opened]:
- **Rule 62-112**: heaters installed so adjacent combustible materials are not subjected to temperatures above **90 °C**.
- **Rule 62-202**: each enclosed area with a heater has a temperature control device.
- **Rule 62-222**: sauna heaters must be:
  - marked as suitable for the purpose;
  - installed per the nameplate;
  - fastened so the nameplate clearances cannot be reduced;
  - not installed below showers or water sprays;
  - **controlled by a timed cut-off switch with a maximum setting of 1 hour and no override**, mounted on the outside wall of the room (unless it is part of the heater or cabinet) and disconnecting all ungrounded conductors.

The OESC is the CEC with Ontario amendments, so expect the same rules in BC's C22.1-24, but I did not read the CEC text. **Gap.**

**Implication for Vantage Access:**
- A booking system that pre-heats and runs back-to-back sessions must not let any heater cycle exceed 60 minutes or be extended remotely.
- Design each booking as one fresh 60-minute cycle. Consider requiring a local action at the door (an NFC tap or push button) to start a cycle.
- Get written interpretations from ESA, the City of Vancouver Electrical Inspection Branch and the City of Victoria on whether an app-initiated cycle counts as an "override".

### 3.3 Product standard

- **CSA C22.2 No. 164:18 (R2022), *Electric sauna heating equipment*** (2nd edition, replaces the 1991 edition). It covers "permanently-connected electric sauna (dry bath) heating equipment **rated 300 V or less**". Clause 8 covers "the combination of a sauna heater or heater unit and a **prefabricated, factory-built room** or cabinet". [CSA Group store](https://store.csastandards.org/store/product/2425995/) [page opened]. This is the Canadian twin of UL 875 configuration (b) in the US research. Vantage can seek a bi-national listing of the whole module (UL 875 + C22.2 No. 164 Clause 8) with one test program.
- Intertek's notice on the revised C22.2 No. 164 says new products are evaluated to the new edition. [Intertek standard update](https://cdn.intertek.com/www-intertek-com/dms-legacy/CSA-C22-2-No-164-Rev-2-1-2018-ED-2-21-2020.pdf) [search excerpt only]
- Some European makers certify to **CSA E60335-2-53** (the IEC-based sauna heater standard) instead. Harvia's Spirit page cites "UL875" for the USA and "CSA E60335-2-53" for Canada. [Harvia Spirit](https://www.harvia.com/en-US/harvia-spirit-electric-heater/) [page opened]

### 3.4 Certification marks accepted

- Accepted: **CSA**, **cUL / cULus** (UL), **cETL / cETLus** (Intertek), and other SCC-accredited bodies' marks such as QPS, TÜV, SGS and Nemko. [ESA list](https://esasafe.com/electrical-products/recognized-certification-marks/) [page opened]
- Intertek: the "c" at 8 o'clock means the product meets Canadian standards and the "us" at 4 o'clock means US standards; **ETL with "US" only = US standards only**. [Intertek, Certification marks compared](https://www.intertek.com/products-retail/certification-marks-comparing-the-differences-fs) [search excerpt only]
- CE marks are not electrical safety approvals in Canada. [ESA Toolbox Talks, Nov 2025](https://esasafe.com/assets/files/esasafe/pdf/Contractor/Toolbox-Talks-Nov-2025.pdf) [search excerpt only]
- Fallback for an uncertified item: an **SPE-1000 field evaluation** by CSA, Intertek, QPS or ESA, unit by unit on site. Recognized in both provinces (same sources). Cost not found; my estimate is CAD 2–6k per evaluation.

### 3.5 Do the heaters on the market carry Canadian certification?

| Heater | US listing seen | Canadian evidence found | Status |
|---|---|---|---|
| Harvia Virta Pro HL16U1UL / HL20U3UL (commercial, 208 V 3-phase for the 20 kW) | "ETL" on Harvia US pages | None on the product page; no "c" mark shown | **Unconfirmed**: ask Harvia North America for the cETLus file number. [Harvia Virta Pro 20](https://www.harvia.com/en-US/products/HL20U3UL/virta-pro-20-kw-208v-black) [page opened] |
| Harvia Spirit | UL 875 | Page states compliance with CSA E60335-2-53 for Canada | **Likely certified for Canada** (manufacturer claim). [Harvia Spirit](https://www.harvia.com/en-US/harvia-spirit-electric-heater/) [page opened] |
| HUUM UKU / DROP | UL 60335-1 | Reseller: CAN/CSA E60335-2-53 via SGS | Reseller claim only. [The Sauna Heater, HUUM listings](https://thesaunaheater.com/pages/huum-sauna-heater-ul-listings) [search excerpt only; 429] |
| HUUM HIVE 12/15/18 (the commercial models) | None found (reviews say SGS/CE) | None | **Not certified for Canada on current evidence.** [Haven of Heat HIVE review](https://havenofheat.com/blogs/sauna-guides/huum-hive-review) [search excerpt only] |
| Saunum Air | Retailers say "UL" | None | Unconfirmed. [Sauna Marketplace, Saunum Air](https://saunamarketplace.com/product/saunum-air/) [search excerpt only] |
| Amerec Pro (10.5 / 14.4 kW, 208 or 240 V, 1- or 3-phase) | Retailers say "UL listed" | None | Unconfirmed. [The Sauna Heater, Amerec Pro 14](https://thesaunaheater.com/products/pro-14) [search excerpt only] |
| Finnleo commercial | n/s | None found | Unconfirmed |

Action: before quoting in Canada, collect the certificate of compliance (file number plus standard) for each heater from the certification body's directory (UL Product iQ, Intertek Directory, CSA certified products list). **Gap.**

### 3.6 600 V supply and what it means for 208/240 V heaters

- BC Hydro's standard three-phase services include **120/208 V wye** and **347/600 V wye**. [BC Hydro service voltages](https://app.bchydro.com/accounts-billing/electrical-connections/electrical-service-voltages.html) and [standard ES54 S2-01](https://app.bchydro.com/content/dam/BCHydro/customer-portal/documents/distribution/standards/ds-ES54-S2-01-secondary-three-phase-services-120-208V-and-347-600V-up-to-1600A.pdf) [search excerpt only]. Toronto Hydro supplies 347/600 V and recently raised its maximum 347/600 V secondary service from 100 A to 200 A for road-allowance supply. [Toronto Hydro Conditions of Service rev. 24](https://www.torontohydro.com/documents/d/guest/conditions-of-service-revision-24-summary-nov-2024) [search excerpt only]. In larger buildings the usual pattern is 600 V distribution with dry-type step-down transformers to 120/208 V panels. [Study guide](https://open-exam-prep.com/study-guides/are-ppd/plumbing-electrical-systems/electrical-service-power) [search excerpt only]
- Since C22.2 No. 164 heaters are rated **300 V or less**, a 600 V-only roof feed needs a **600 V delta to 208Y/120 V transformer**.
- **Current at 208 V three-phase** (my arithmetic, I = P/(√3·208)):
  - Perch 10.5 kW: 29 A (or 44 A at 240 V single-phase).
  - Lodge 18 kW: 50 A.
  - Summit 24 kW: 67 A, plus chiller, pumps and lights.
- **Transformer size (estimate)**: continuous heater load × 1.25 plus about 2 kVA for controls, fans and lights. Perch about 16 kVA (use **30 kVA**, the next practical size), Lodge about 25 kVA (**30 kVA**), Summit about 38 kVA (**45 kVA**).
- **Hardware price**: a Hammond 45 kVA, 600 V delta to 208Y/120 V, aluminium-wound, 385 lb unit lists at **$3,457.99** at a US retailer (currency not stated). [HomElectrical](https://www.homelectrical.com/electric-transformers/hammond-hps-sg3a0045pb.1.html) [page opened]. The copper-wound Canadian part EG3A0045PBC is stocked by Futech, with no price shown. [Futech](https://shop.futech.ca/en/Catalog/Details/HP.EG3A0045PBC) [page opened]
- **Installed cost (estimate): CAD 10–25k** per site. That covers the 600 V feeder breaker, the transformer in a 3R enclosure on the roof or in an electrical room, the secondary panel, grounding, mounting, labour and permit. The range depends on the run length from the electrical room.
- **208 V buildings: do not install 240 V-rated heaters.** Output scales with voltage squared: (208/240)² ≈ 0.75, so an 18 kW 240 V heater gives about 13.5 kW on 208 V. A vendor guide gives the same ratio (4.5 kW → about 3.4 kW). [Haven of Heat, 240 V vs 208 V](https://havenofheat.com/zh/blogs/sauna-guides/sauna-wiring-240v-vs-208v-explained) [search excerpt only]. Specify heaters nameplated for 208 V three-phase (Harvia's HL20U3 is 208 V three-phase), and make the Perch heater a 208 V model too.

---

## 4. Accessibility

### 4.1 What applies

- **BC and Vancouver: BCBC 2024 Section 3.8** (VBBL follows it; Vancouver changes were not read). It references **CSA B651-18** as an alternative design route for each element (Table 3.8.3.1). An accessible path is required "within all other normally occupied areas", but "access is not required … (f) to attic or roof spaces". Whether an amenity roof is a "roof space" is a question for the building official; the sensible reading is that it is a normally occupied area. Alterations: access "where … practical". [BCBC 2024 3.8](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]
- **Ontario: OBC 2024 Section 3.8 "barrier-free"**. A barrier-free path is required "within all normally occupied floor areas **and rooftop amenity spaces**". [OBC 3.8.2.1.(1)(b)](https://www.ontario.ca/document/2024-building-code-compendium/part-3-fire-protection-occupant-safety-and-accessibility) [code text read]. OBC also references CSA B651-18. [OBC Div B Table 1.3.1.2](https://www.ontario.ca/document/2024-building-code-compendium/part-1-general) [code text read]
- **AODA (Ontario)**: the Design of Public Spaces Standards cover outdoor public spaces, such as trails, outdoor eating and play areas, exterior paths of travel and parking, plus service counters and waiting areas. They apply to new or redeveloped spaces. Building interiors such as entrances, washrooms and paths of travel "are addressed through Ontario's Building Code". [Queen's University AODA summary](https://www.queensu.ca/accessibility/across-campus/aoda/integrated-accessibility-standards-regulation-iasr/design-public-spaces) [page opened]. So for a rooftop sauna the OBC governs. Hotels selling sessions must also follow AODA's customer service standard (not researched in detail).
- **BC**: the Accessible British Columbia Act has no built-environment standard yet. The first standards are employment and service delivery. [BC accessibility standards](https://www2.gov.bc.ca/gov/content/governments/about-the-bc-government/initiatives/accessibility/standards) [search excerpt only]
- **No sauna-specific provisions.** Neither BCBC nor OBC Section 3.8 mentions saunas. ADA 612 (accessible sauna, bench, turning space) has no Canadian equivalent. Search of both code texts: "sauna" appears only in energy and fire-detector notes [code text read].

### 4.2 Comparison with the ADA-based spec

| Item | Current spec (ADA) | BC: BCBC 2024 / VBBL | Ontario: OBC 2024 | Change for Canada |
|---|---|---|---|---|
| Door clear width | 813 mm (32 in) | **850 mm** (3.8.3.6.(2)) | **850 mm** (3.8.3.3.(1)) | 850 mm minimum; target 900 mm leaf |
| Door opening force | 5 lbf (22 N) | 38 N exterior, 22 N interior (3.8.3.6.(8)) | 38 N exterior, 22 N interior (3.8.3.3.(7)) | Keep 22 N or less |
| Threshold | 13 mm | 13 mm or less, bevelled (3.8.3.6.(5)) | Level, or bevelled 13 mm or less | No change |
| Clear floor at door | ADA maneuvering clearances | Pull side **1,700 × 1,500 mm**; push side 1,200 × 1,500 mm; latch-side clearance 600 / 300 mm (3.8.3.6.(11),(14),(15)) | Level area the width of the door plus latch clearance × up to 1,500 mm; latch side 600 / 300 mm (3.8.3.3.(10),(13)) | Perch porch and Lodge/Summit vestibule must fit 1,700 × 1,500 on the pull side |
| Turning space | 1,525 mm circle | 1,700 mm in universal washrooms (3.8.3.13); 1,700 mm turning spaces at long narrow paths (3.8.3.2.(6)) | 1,700 mm in universal washrooms; **1,500 mm** in vestibules with non-aligned doors (3.8.3.3.(11)) | **Use 1,700 mm** in Lodge/Summit vestibules and changing rooms |
| Vestibule, doors in series | n/s | 1,350 mm plus any door swinging in (3.8.3.6.(12)) | **1,500 mm** plus any door swinging in (3.8.3.3.(11)) | Use 1,500 mm plus swing |
| Path width | 915 mm | 1,000 mm (850 mm for 600 mm or less of length) (3.8.3.2) | **1,100 mm** (3.8.1.3.(1)) | 1,100 mm on porch and route |
| Walking surface openings | 13 mm | **13 mm sphere maximum**, elongated openings perpendicular to travel (3.8.3.2.(3)) | Same (3.8.1.3.(2)) | Floor grating mesh 13 mm or less |
| Glass door marking | n/s | Contrasting door or frame for public-corridor doors (3.8.3.6.(17)) | All-glass doors: opaque contrasting strip at least 50 mm wide at 1,350–1,500 mm height; vision panel bottom 900 mm or less (3.8.3.3.(14),(15)) | Add a manifestation strip to the glass door |
| Controls | ADA 309 | CSA B651 cl. 4.2 route (Table 3.8.3.1) | 900–1,100 mm high, closed-fist operation, 22.2 N or less (3.8.1.5) | Smart lock reader and heater controller at 900–1,100 mm |
| Power door operator | No | Only where 3.8.2.7 requires | Required on doors serving "a Group A occupancy within a Group C major occupancy apartment building" (3.8.3.3.(6)) | Ask Toronto Building whether a sauna amenity in a rental or condo tower is "Group A". If yes, add an operator option |
| Showers | ADA 608 if provided | Outside residential suites, "at least one shower stall in **each group** of showers" must be accessible, **even a single shower**: 1,500 × 900 mm, 900 mm clear floor, two grab bars, folding seat 450 × 400 at 460–480 mm. Where showers serve "the general public or customers", a **universal dressing and shower room** is also required (3.8.2.8.(12),(13); 3.8.3.17) | A group of 1 shower needs 0 barrier-free showers; 2–7 need 1 (Table 3.8.3.13) | **BC Lodge: redesign the vestibule shower as an accessible stall**, or remove it. BC hotels: make the Lodge/Summit changing room a universal dressing and shower room |
| Route to the roof | Building's responsibility | Normally occupied areas; "roof spaces" exception; "where practical" for alterations | **Required to rooftop amenity spaces** | Ontario site filter: elevator or platform lift to roof level. BC: confirm with the building official |
| Sauna bench | ADA 903 transfer bench | None | None | Keep the ADA bench (450–480 mm high, 1,070 × 510–610 mm) as best practice |

Sources: [BCBC 2024 3.8](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) and [OBC 2024 Part 3](https://www.ontario.ca/document/2024-building-code-compendium/part-3-fire-protection-occupant-safety-and-accessibility) [code text read]; ADA figures from `research/sauna-design-research.md` section 5.

---

## 5. Cranes, street use and elevator delivery

### 5.1 Street-use and crane permits

| City | Rule | Fees | Lead time | Source |
|---|---|---|---|---|
| Vancouver | No one may occupy a street "or the air space above a street" for building work without a street use permit from the City Engineer. Lane, bike-lane, sidewalk and alley closures carry lane-use fees (Street & Traffic By-law s.30) | Not found | Temporary street occupancy: apply **7 working days** before the start; **7–10 business days** to process after payment | [City of Vancouver, temporary street occupancy](https://vancouver.ca/streets-transportation/reserve-metered-spaces.aspx) and [construction street use permits](https://vancouver.ca/home-property-development/construction-street-use-permits.aspx) [search excerpt only; 403] |
| Victoria | A Street Occupancy Permit is needed for anything on the right-of-way | Per 13 m² per day: sidewalk **$10**, metered roadway **$20**, unmetered **$15**; lane closure **$25 per lane per day**; parking reservation $40 (2024) | Minimum 2 business days (5 if residential parking is removed). Recommended 1 week (minor), 2 weeks (intermediate), **2 months** (major arterial impacts) | [City of Victoria info sheet, 2024](https://www.victoria.ca/media/file/street-occupancy-permitinfo-sheet) [page opened] |
| Toronto | A Street Occupation Permit is needed for "hoisting with a mobile crane or boom truck". Permits are obtained in person | 2026: hoisting **$73.89 + HST per day**; **$178.81** per additional lane per day; **$894.03** per full lane closure per day; roadway occupation $42–204 per m² per month by area. Construction Hubs: +25% (hoisting $92.35 per day) | Tower crane boom swing: "approximately **12 weeks**". No figure given for mobile crane permits | [City of Toronto, Street Occupation Permit](https://www.toronto.ca/services-payments/building-construction/infrastructure-city-construction/construction-standards-permits/right-of-way-construction-permits/street-occupation-permit/) [page opened] |

**Operators**
- BC: mobile cranes and boom trucks may only be operated by a certified operator (WorkSafeBC OHS Regulation s.14.34.1, administered by BC Crane Safety). [WorkSafeBC](https://www.worksafebc.com/en/health-safety/education-training-certification/crane-operator) [search excerpt only]
- Ontario: Hoisting Engineer, Mobile Crane Operator 1 is a compulsory trade. Cranes over 30,000 lb capacity need an MCO 1 holder (O. Reg. 213/91 s.150, as amended by O. Reg. 88/13). [O. Reg. 88/13](https://www.ontario.ca/laws/regulation/r13088) [search excerpt only]

**Crane cost**
- No Canadian rate card was found on an opened page. A Turner & Townsend survey (via Statista) ranked **Vancouver third most expensive** of the cities surveyed in 2025 for a 50-tonne mobile crane with operator for a day, after New York and Houston. [Statista](https://www.statista.com/statistics/1340453/mobile-crane-costs-global-by-city) [search excerpt only]
- **Estimate**:
  - Perch or Lodge as a module to a mid-rise roof (20–40 m, 3–5 t pick): 100–150 t all-terrain crane, **CAD 6–12k per lift day all-in** (crane, operator, rigging crew, traffic control, permit).
  - Summit (about 8 t module, plus plunge) on a 25–30 storey tower (about 90 m, with radius): 250–350 t class with counterweight trucks, **CAD 20–45k per day**.
  - Basis: US bid rates of $630–1,100 per hour for 80–120 t cranes ([Steuben County bid](https://steubencountyny.gov/Archive.aspx?ADID=2773) [search excerpt only]), scaled up for size, mobilization and urban traffic control. **Get three quotes per city.**
  - Implication: limit Summit to mid-rise roofs or new builds with a tower crane, or develop a panelized Summit.

### 5.2 Elevator delivery norms

- Where a building has elevators, at least one must fit "a patient stretcher **2,010 mm long and 610 mm wide** in the prone position" (LULA elevators excepted). [BCBC 2024 3.5.4.1](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf) [code text read]. That is the only code-guaranteed size. It does not guarantee room for a **2.3 × 1.2 m** panel laid flat, and stood upright the panel needs a car at least 2.3 m high inside.
- **Change (estimate):** cap panels at **2.0 × 1.1 m**, so they fit any stretcher-compliant car flat or on the diagonal. Keep pieces at 120 kg or less. Check the actual car size and door opening on the site survey.
- Many elevators stop one floor below the roof. The last flight is by stair, where 120 kg pieces need 4 people or a stair-climber. Add a stair-climber or a temporary davit hoist to the install kit.

---

## 6. Health and safety rules for saunas and cold plunges

### 6.1 British Columbia: Pool Regulation (B.C. Reg. 296/2010, consolidated to 27 Oct 2026)

- "Pool" means "a commercial pool, hot tub, public pool, spray pool or wading pool".
- **"Commercial pool"** = an artificial body of water that "has a depth of at least **61 cm**" and is owned or operated by (or with):
  - an accommodation business with rooms for the public (but not one with **fewer than 4 units**);
  - a membership-only business; or
  - **a strata corporation**;

  and is used only by members, tenants, patrons or their guests.
- Below 61 cm it is a **"wading pool"**, which is still a pool.
- Exempt: pools "drained and cleaned after each use", single-family or duplex pools not owned by a strata, pools inside an individual hotel room, and enterprises with fewer than 4 units.
- **Construction permit** from a health officer, with plans "prepared, sealed, and certified by an engineer or architect" (s.5). **Operating permit**, renewed yearly, with an engineer or architect statement and a pool safety plan (s.6).
- Water rules: free chlorine at least **0.5 ppm** at 30 °C or below (1.5 ppm above 30 °C), tested **twice daily**; combined chlorine under 1 ppm; pH 7.2–7.8; alkalinity 80–120 ppm; turnover at the design flow rate.
- [BC Pool Regulation](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/296_2010) [page opened]
- **Is a cold plunge a pool?** Yes. A 1,200 L shared plunge at a hotel, a serviced-apartment business (4 or more units) or a strata is a commercial pool if 61 cm or deeper, otherwise a wading pool. It is not a "hot tub" (defined as hydrotherapy or swirl pools). Whether a long-term **rental** landlord counts as "a business enterprise that maintains private rooms … for the accommodation of the public" is unclear. Ask VCH or Island Health. **Gap.** Ozone/AOP alone does not meet the chlorine (or bromine) residual rules.
- **Saunas**: no BC public-health sauna rule was found. The old Personal Service Establishments Regulation, which listed saunas, was repealed in 2011. A 2026 national review says "saunas are not regulated or routinely inspected by environmental public health professionals in most provinces and territories". [NCCEH sauna rapid review, 2026](https://ncceh.ca/resources/evidence-briefs/rapid-review-environmental-health-risks-and-safety-considerations-saunas) [search excerpt only; 403]. In June 2024 Vancouver council asked staff to request that Vancouver Coastal Health develop a regulatory framework for outdoor cold plunge and sauna businesses. [Council motion](https://council.vancouver.ca/20240626/documents/cfscA3.pdf) and [CBC](https://amp.cbc.ca/news/canada/british-columbia/hot-saunas-cold-plunges-1.7246528) [search excerpt only]. Rules may tighten; watch this.

### 6.2 Ontario: Reg. 565 Public Pools (amended by O. Reg. 502/24, in force 1 Jan 2025)

- New definition: **"Public Cold Plunge Pool" means a pool that is maintained at a temperature of 15 °C or less, with or without hydrojets, that is not drained, cleaned, sanitized and refilled before use by each individual.** [Halton Pool and Spa Operator Guide, updated 5 Sep 2025](https://www.halton.ca/Repository/Pool-Owner-Operator-Information-Package) [page opened]
- **Class B pools** include pools at "an apartment building that contains **six or more** dwelling units", a hotel "for the use of its guests", a club, or "a condominium … that contains six or more dwelling units" (Reg. 565 s.2). Cold plunge pools are inspected as Class A or Class B pools. A pool "to which the general public is admitted" is Class A, so a hotel plunge sold to outside (non-guest) customers would be a Class A pool. ([Reg. 565 s.2](https://www.ontario.ca/laws/regulation/900565) [regulation text read, fact-check 2026-11-01]); [Halton guide](https://www.halton.ca/Repository/Pool-Owner-Operator-Information-Package) [page opened]; [Simcoe Muskoka health unit letter, 28 Jan 2025](https://www.simcoemuskokahealth.org/docs/default-source/topic-safewater/2024-reg-565-amendments-final.pdf) [page opened]
- Cold plunge requirements:
  - non-slip deck at the entrance;
  - **handrail** for entry and exit;
  - prescribed **caution sign** (no under-12s unsupervised, cold-shock warning);
  - a **clock** visible from the pool (s.26.0.1);
  - free chlorine residual **5–10 ppm** for cold plunge pools ([Reg. 565 s.7(8)(e.1), as amended by O. Reg. 502/24](https://www.ontario.ca/laws/regulation/900565) [regulation text read, fact-check 2026-11-01]).
  - General Class B rules also apply, including an emergency stop button for pumps, an emergency telephone within 30 m, and daily logs.
  - **Notify public health at least 14 days before opening** after construction or alteration.
  - [Halton guide](https://www.halton.ca/Repository/Pool-Owner-Operator-Information-Package) [page opened]
- "Public spa" means a hydro-massage pool (jets or air bubbles over most of the pool). A still-water cold plunge is a cold plunge pool, not a spa. [Halton guide](https://www.halton.ca/Repository/Pool-Owner-Operator-Information-Package) [page opened]
- **Saunas**: no Ontario public-health sauna regulation was found. The Fire Marshal and ESA notice (section 1.4) is the main safety guidance.

---

## 7. Design changes needed for Canada

| # | Current US spec item | Canadian requirement | Change |
|---|---|---|---|
| 1 | Base: ballast trays + parapet tie-back, **zero penetrations** | BC/ON 4.1.8.18: Vp = 0.3·S(0.2)·IE·Sp·Wp with Ax = 3 on the roof; **friction may not resist earthquake forces**; solar-array exception excludes occupied roofs. Vancouver and Victoria are SC4 | Two base variants. **BC: engineered, flashed structural anchors (4–8 posts) designed for about 0.8–2.7 × module weight laterally; minimize ballast.** Ontario: ballast base allowed only if SC1/SC2 and classed as equipment, checked for wind |
| 2 | "Designed for occupiable roofs rated 100 psf (4.8 kPa)" | Same 4.8 kPa (4.1.5.5.(3), Table 4.1.5.3); ordinary roofs 1.0 kPa; Ontario Part 11 remedial-work rule | Restate in kPa with NBC/BCBC/OBC references. Publish point loads per foot, including the seismic anchor reactions for BC |
| 3 | Module roof and snow (not specified) | Basic roof snow 1.64 kPa Vancouver, 1.82 kPa Vancouver Granville, 1.08–1.50 kPa Victoria, 1.12 kPa Toronto; drift beside projections (4.1.6.7) | Design the module roof for **2.0 kPa plus drift**; give the engineer a drift-zone diagram; keep host drains out of the drift zone |
| 4 | Wind to ASCE 7 (GCr 1.9/1.5) | NBC 4.1.7 static procedure, q1/50 = 0.45 (Vancouver), 0.57 (Victoria), 0.44 (Toronto) kPa; no CFD | Redo base and tie-down calculations to NBC 4.1.7 |
| 5 | Full-length tempered IGU glass front | Glass fallout check at 1.25 × drift in SC3/SC4 (4.1.8.18.(14)) | Specify glazing frame clearance or a laminated inner lite for BC |
| 6 | Heater "ETL/UL 875 listed" | Canadian mark (cETLus / cULus / CSA) to **CSA C22.2 No. 164-18** or CSA E60335-2-53; US-only marks not accepted | Specify bi-nationally marked heaters and collect certificate numbers. **Seek a module listing to C22.2 No. 164 Clause 8 + UL 875 (b)** |
| 7 | 208–240 V 3-phase heaters | Services are 120/208 V or 347/600 V; heaters are 300 V or less (C22.2 No. 164) | Specify **208 V-rated** heaters (no 240 V heaters on 208 V). Offer a **600 V delta to 208Y/120 V transformer kit**: 30 kVA Perch/Lodge, 45 kVA Summit, about CAD 10–25k installed (estimate) |
| 8 | 60-minute session timer, remote schedules, emergency stop | OESC 62-222: **timed cut-off, max 1 h, no override**, mounted outside the room; 62-202 thermostat; 62-112 combustibles 90 °C or less | Hard-wired 1-hour no-override timer in series with the controller; app cannot extend a cycle; pre-heat within the cycle. Get ESA, Vancouver and Victoria interpretations on app-started cycles |
| 9 | 90 °C interior cap | Consistent with listed heaters and 62-112 | Keep; document heater clearances per the nameplate |
| 10 | Door 813 mm clear, outward glass door | **850 mm** clear in both provinces; 22 N interior / 38 N exterior force; Ontario: opaque strip 50 mm wide at 1,350–1,500 mm on glass doors, vision panel 900 mm or less | 850 mm minimum (target 900 mm leaf); add a glass manifestation strip; adjust closers |
| 11 | 1,525 mm turning circle in vestibule or porch | 1,700 mm universal-washroom standard; 1,700 × 1,500 mm pull-side clear floor (BC); Ontario vestibule 1,500 mm plus door swing | **1,700 mm** turning space in Lodge/Summit changing rooms; recheck the Perch porch for 1,700 × 1,500 |
| 12 | Lodge vestibule 2.8 × 1.6 m with indoor shower | BC: every shower group (even one shower) needs an accessible stall 1,500 × 900 + 900 mm clear floor, grab bars, seat; hotels with showers for customers need a universal dressing and shower room. Ontario: a single shower is exempt | BC variant: enlarge the vestibule or replace the shower with an exterior rinse; hotel variant: universal dressing and shower room |
| 13 | Aluminium grating sub-floor with composite decking | Openings 13 mm or less on the accessible path; stable, firm, slip-resistant | Specify 13 mm-or-less openings, oriented perpendicular to travel |
| 14 | Thermally modified ash cladding | Noncombustible buildings: combustible cladding only if sprinklered throughout and the assembly passes CAN/ULC-S134 | **Noncombustible cladding option** (aluminium or steel wood-look, fibre cement) for towers, or fund an S134 test |
| 15 | 15 mm thermo-aspen interior lining | Noncombustible buildings: walls flame-spread 150 or less; **ceilings 25 or less** (or FRT wood) | Test the boards to CAN/ULC-S102; plan an FRT or alternative-solution ceiling for tower jobs |
| 16 | No sprinkler provision | Sprinklered buildings (NFPA 13): saunas typically get 286 °F heads | Sprinkler-ready module: dry-pendent high-temperature head in the hot room, standard head in the vestibule, connection stub, freeze protection |
| 17 | No fire alarm or egress spec | Alarm audible throughout any occupancy on a roof; roof exit designed as an exit; 2 exits if more than 60 occupants; 1,070 mm non-climbable guards | Horn/strobe inside the module tied to the building; site filter: exit stair to roof, guard height, occupant load |
| 18 | Rooftop enclosure height (not addressed) | A sauna is not in the 3.2.1.1 list of enclosures excluded from building height | Code-consultant opinion per building type; avoid 6-storey wood buildings until resolved |
| 19 | Panels up to 2.3 × 1.2 m, 120 kg or less | Only a 2,010 × 610 mm stretcher car is code-guaranteed (3.5.4.1) | **Panels 2.0 × 1.1 m or smaller**; stair-climber or davit in the install kit |
| 20 | No factory certification | CSA A277: optional, but gives "deemed to comply" in Ontario (Div C 1.12.1.1) and avoids re-inspection in BC | Certify the factory and kit to **CSA A277** through an SCC-accredited body |
| 21 | Cold plunge 1,200 L, 2 HP chiller, ozone/AOP | BC: commercial or wading pool, construction and operating permits, chlorine 0.5 ppm or more (30 °C or below), tested twice daily. Ontario: Class B public cold plunge pool, free chlorine 5–10 ppm, handrail, non-slip deck, clock, caution sign, emergency stop, 14-day notice | Add chlorine or bromine dosing with an auto-controller and logging, handrail, clock, prescribed signs and an emergency stop. Price health permits into the Summit and plunge add-on. Consider a drain-after-each-use plunge to stay outside both regulations |
| 22 | Install lead time 6–10 / 10–14 weeks | Ontario 20–30 business-day permit clock; Vancouver about 32-day median; owner votes; pool permits; street use | Quote **12–20 weeks (Perch/Lodge) and 16–26 weeks (Summit)** for Canada (estimate) |
| 23 | Crane assumed for Summit | Street occupation permits in all three cities; certified operators; Toronto tower crane swing about 12 weeks | Default to panel kits; crane only with a staging street; Summit limited to mid-rise roofs or panelized |

---

## 8. Gaps

1. **Site-specific seismic values.** I could not query the NRCan 2020 seismic hazard tool (HTTP 403). The Vp table uses the Part 9 Smax values as a lower bound for S(0.2). Run the tool for every site, with the geotechnical site class. Confirm Toronto's Seismic Category, which could be SC3 on soft sites.
2. **Vancouver Building By-law 2025 text** (vancouver.ca blocked). Confirm any Vancouver changes to 3.2.1.1, 3.1.5, 3.8, 4.1.8.18 and Part 11, and the 15 Sep 2026 seismic start date.
3. **CEC 2024 (C22.1-24) sauna rule text.** Rule 62-222 was taken from the Ontario ESA notice. Confirm the BC wording and whether any exception exists for commercial or attended saunas. Get written interpretations on app-started heater cycles.
4. **Canadian certificates for specific heaters** (Harvia Virta Pro, HUUM HIVE, Saunum, Amerec, Finnleo). Not found in certification directories; manufacturer or reseller claims only.
5. **Whether the module counts as a "storey"**, and whether the building official treats it as equipment (Category 11) or a penthouse (Category 5). These are authority interpretations; get pre-application opinions in each city.
6. **Sprinklers in saunas.** Only field practice was found (286 °F heads). Confirm with the NFPA 13 edition referenced by NBC 2020 and with each fire department.
7. **Flame-spread ratings** of thermo-aspen (interior) and thermo-ash (cladding). Commission CAN/ULC-S102 tests and decide on an S134 test.
8. **Crane rates and Vancouver street-use fees.** No primary rate card or Vancouver fee schedule was opened. Get three quotes per city.
9. **Victoria building permit timelines.** Not published; ask at a pre-application meeting.
10. **BC Pool Regulation scope for long-term rental landlords.** Ask VCH and Island Health. Also, plunge permit fees and processing times in BC, and Toronto Public Health's plan-review practice.
11. **Toronto barrier-free path to the roof on existing buildings.** How OBC 3.8.2.1 ("rooftop amenity spaces") applies when only the rooftop amenity is new work under Part 11. This is a critical site filter.
12. **Zoning.** Vancouver's 3.6 m rooftop amenity structure relaxation and Toronto's rooftop structure rules were seen only as excerpts. Confirm whether enclosed saunas qualify, and the variance timelines (Toronto Committee of Adjustment).
13. **Strata and condo approval thresholds.** *Checked against the statute text on fact-check 2026-11-01.* BC s.71 still needs a 3/4 vote (a majority vote applies only to EV-charging changes). Ontario s.97(4) needs owners of at least 66⅔% of all units to vote in favour of a substantial change.
14. **Energy and green rules** (BC Energy Step Code or Part 10, Vancouver energy requirements, NECB, Toronto Green Standard) for a heated rooftop enclosure. Not researched.
15. **Costs.** CSA A277 certification, SPE-1000 field evaluations, transformer installation and Canadian electrical and structural sub rates are estimates. Get quotes.
16. **How common 600 V-only roof feeds are.** No data on how many Vancouver, Victoria and Toronto hotels or rental towers lack a usable 120/208 V supply at roof level. Add to the site survey checklist.
17. **AODA customer service obligations for hotels selling sauna sessions.** Not researched in detail.

---

## Sources (all accessed 2026-11-01)

Codes and code bodies
- British Columbia Building Code 2024, web version revision 2 (full PDF; read 3.1.5, 3.2.1.1, 3.2.2.14, 3.2.4.18, 3.3.1.3, 3.3.1.18, 3.5.4.1, 3.8, 4.1.5, 4.1.6, 4.1.8.18, Appendix C Tables C-2 and C-3, Note A-1.1.1.1.(3)): https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/revisions-and-mo/bcbc_2024_web_version_revision2.pdf [code text read]
- BC Codes 2024 page: https://www2.gov.bc.ca/gov/content/industry/construction-industry/building-codes-standards/bc-codes/2024-bc-codes [page opened]
- BC Bulletin B24-02-R, seismic transition (19 Sep 2024): https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/bulletins/2024-code/b24-02-r_seismic_design_delay_period_final.pdf [page opened]
- City of Vancouver, Guide to 2025 VBBL updates: https://vancouver.ca/files/cov/guide-to-2025-vbbl-updates.pdf [search excerpt only; 403]
- bccodes.ca, Vancouver by-laws: https://bccodes.ca/vancouver-bylaws.html [search excerpt only]
- City of Vancouver, Code Change 24-0030 Existing Buildings: https://vancouver.ca/files/cov/ccr-24-0030-existing-buildings.pdf [search excerpt only]
- Ontario 2024 Building Code Compendium (O. Reg. 163/24), read on ontario.ca:
  - Part 4 Structural Design: https://www.ontario.ca/document/2024-building-code-compendium/part-4-structural-design [code text read]
  - Part 3 Fire Protection, Occupant Safety and Accessibility: https://www.ontario.ca/document/2024-building-code-compendium/part-3-fire-protection-occupant-safety-and-accessibility [code text read]
  - SB-1 Climatic and Seismic Data: https://www.ontario.ca/document/2024-building-code-compendium/sb-1-climatic-and-seismic-data [code text read]
  - Division C Part 1 (1.3.1.3, 1.12.1.1): https://www.ontario.ca/document/2024-building-code-compendium/part-1-general-0 [code text read]
  - Division B Part 1 (Table 1.3.1.2): https://www.ontario.ca/document/2024-building-code-compendium/part-1-general [code text read]
  - Part 11 Renovation: https://www.ontario.ca/document/2024-building-code-compendium/part-11-renovation [code text read]
- The 2024 Ontario Building Code page: https://www.ontario.ca/page/2024-ontario-building-code [search excerpt only]
- OAA, end of OBC transition period: https://oaa.on.ca/whats-on/news-and-insights/news-and-insights-detail/Ontarios-2024-Building-Code-End-of-the-Transition-Period [search excerpt only]
- City of Victoria, Climatic and Seismic Data bulletin (11 Mar 2025): https://www.victoria.ca/media/file/climatic-and-seismic-data-2025-03-11 [page opened]
- CHBA, Code compliance for modular (CSA A277 in Ontario): https://st.chba.ca/CHBADocs/CHBA/Publications/Webinars/2023-01-26-Code-Compliance-for-Modular-Webinar-CHBA.pdf [search excerpt only]
- City of Toronto staff report on modular inspections (2025): https://www.toronto.ca/legdocs/mmis/2025/ph/bgrd/backgroundfile-253704.pdf [search excerpt only]
- MeyerFire, saunas and sprinklers (Mar 2024): https://www.meyerfire.com/daily/saunas-considered-bathrooms-for-sprinklers [page opened]
- NFPA 13 first revision report (temperature ratings table): https://docinfofiles.nfpa.org/files/AboutTheCodes/13/13_A2018_AUT_PRI_FRReport.pdf [search excerpt only]

Permits and timelines
- Technical Safety BC, Jurisdiction: https://www.technicalsafetybc.ca/about-us/jurisdiction [page opened]
- City of Toronto, Building permit review streams: https://www.toronto.ca/services-payments/building-construction/apply-for-a-building-permit/building-permit-review-streams [page opened]
- City of Toronto audit (2024): https://www.toronto.ca/legdocs/mmis/2024/au/bgrd/backgroundfile-243032.pdf [PDF opened, fact-check 2026-11-01]
- City of Vancouver news, permits (Jul 2024): https://vancouver.ca/news-calendar/residents-and-businesses-can-obtain-permits-easier-july-2024.aspx [search excerpt only]
- City of Vancouver permitting fact sheet (Jun 2026): https://vancouver.ca/files/cov/fact-sheet-permitting-improvements-june%202026.pdf [search excerpt only]
- City of Victoria, Building permits: https://www.victoria.ca/building-business/permits-development-construction/building-renovating/building-permits [search excerpt only]
- Vancouver Zoning and Development By-law s.10: https://bylaws.vancouver.ca/zoning/zoning-by-law-section-10.pdf [search excerpt only]
- Toronto zoning amendments and Bill 645 (2026): https://www.toronto.ca/zoning/bylaw_amendments/ZBL_NewProvision_Chapter40.htm, https://www.toronto.ca/legdocs/bills/2026/bill0645.pdf [search excerpt only]
- Strata Property Act s.71 (BC Laws): https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/98043_05 [statute text read, fact-check 2026-11-01]
- BCLI, CRT roundup on Strata Property Act s.71: https://www.bcli.org/?p=13742 [search excerpt only]
- Ontario Condominium Act, 1998 (s.97 read): https://www.ontario.ca/laws/statute/98c19 [statute text read, fact-check 2026-11-01]
- FirstService Residential, Condo common elements (Ontario): https://www.fsresidential.com/ontario/news-events/articles/condo-common-elements/ [search excerpt only]

Electrical
- TSBC IB-EL 2024-01, adoption of BC Electrical Code 2024: https://technicalsafetybc.ca/regulatory-resources/regulatory-notices/information-bulletin-adoption-of-bc-electrical-code-2024-edition [page opened]
- TSBC approved certification marks, B-E3 071019 3 rev. 13: https://www.technicalsafetybc.ca/regulatory-resources/regulatory-notices/approved-certification-marks-electrical-products [page opened]
- ESA, Ontario Electrical Safety Code: https://esasafe.com/role/oesc/ [page opened]
- ESA and OFMEM Flash 25-20-FL, electric saunas (May 2025): https://esasafe.com/assets/files/esasafe/pdf/Electrical_Safety_Products/Flash_Notices/25-20-FL.pdf [page opened]
- ESA recognized certification marks: https://esasafe.com/electrical-products/recognized-certification-marks/ [page opened]
- ESA Toolbox Talks (Nov 2025): https://esasafe.com/assets/files/esasafe/pdf/Contractor/Toolbox-Talks-Nov-2025.pdf [search excerpt only]
- CSA Group, C22.2 No. 164:18 (R2022): https://store.csastandards.org/store/product/2425995/ [page opened]
- Intertek, C22.2 No. 164 standard update: https://cdn.intertek.com/www-intertek-com/dms-legacy/CSA-C22-2-No-164-Rev-2-1-2018-ED-2-21-2020.pdf [search excerpt only]
- Intertek, certification marks compared: https://www.intertek.com/products-retail/certification-marks-comparing-the-differences-fs [search excerpt only]
- UL Canada, Acceptance of Electrical Products in Canada: https://canada.ul.com/wp-content/uploads/sites/11/2018/05/Acceptance-of-Electrical-Products-in-Canada-1.pdf [page opened]
- Harvia Spirit: https://www.harvia.com/en-US/harvia-spirit-electric-heater/ [page opened]
- Harvia Virta Pro 20 kW 208 V: https://www.harvia.com/en-US/products/HL20U3UL/virta-pro-20-kw-208v-black [page opened]
- The Sauna Heater, HUUM UL listings: https://thesaunaheater.com/pages/huum-sauna-heater-ul-listings [search excerpt only; 429]
- Haven of Heat, HUUM HIVE review: https://havenofheat.com/blogs/sauna-guides/huum-hive-review [search excerpt only]
- Sauna Marketplace, Saunum Air: https://saunamarketplace.com/product/saunum-air/ [search excerpt only]
- The Sauna Heater, Amerec Pro 14: https://thesaunaheater.com/products/pro-14 [search excerpt only]
- Haven of Heat, 240 V vs 208 V: https://havenofheat.com/zh/blogs/sauna-guides/sauna-wiring-240v-vs-208v-explained [search excerpt only]
- BC Hydro electrical service voltages: https://app.bchydro.com/accounts-billing/electrical-connections/electrical-service-voltages.html [search excerpt only]
- BC Hydro ES54 S2-01: https://app.bchydro.com/content/dam/BCHydro/customer-portal/documents/distribution/standards/ds-ES54-S2-01-secondary-three-phase-services-120-208V-and-347-600V-up-to-1600A.pdf [search excerpt only]
- Toronto Hydro Conditions of Service rev. 24 summary: https://www.torontohydro.com/documents/d/guest/conditions-of-service-revision-24-summary-nov-2024 [search excerpt only]
- Open Exam Prep, electrical service and power: https://open-exam-prep.com/study-guides/are-ppd/plumbing-electrical-systems/electrical-service-power [search excerpt only]
- HomElectrical, Hammond SG3A0045PB 45 kVA: https://www.homelectrical.com/electric-transformers/hammond-hps-sg3a0045pb.1.html [page opened]
- Futech, Hammond EG3A0045PBC: https://shop.futech.ca/en/Catalog/Details/HP.EG3A0045PBC [page opened]

Accessibility
- Queen's University, AODA Design of Public Spaces summary: https://www.queensu.ca/accessibility/across-campus/aoda/integrated-accessibility-standards-regulation-iasr/design-public-spaces [page opened]
- BC accessibility standards: https://www2.gov.bc.ca/gov/content/governments/about-the-bc-government/initiatives/accessibility/standards [search excerpt only]

Cranes and street use
- City of Toronto, Street Occupation Permit (2026 fees): https://www.toronto.ca/services-payments/building-construction/infrastructure-city-construction/construction-standards-permits/right-of-way-construction-permits/street-occupation-permit/ [page opened]
- City of Vancouver, temporary street occupancy: https://vancouver.ca/streets-transportation/reserve-metered-spaces.aspx [search excerpt only; 403]
- City of Vancouver, construction street use permits: https://vancouver.ca/home-property-development/construction-street-use-permits.aspx [search excerpt only]
- City of Victoria, Street Occupancy Permit info (2024): https://www.victoria.ca/media/file/street-occupancy-permitinfo-sheet [page opened]
- Statista / Turner & Townsend, mobile crane costs by city: https://www.statista.com/statistics/1340453/mobile-crane-costs-global-by-city [search excerpt only]
- Steuben County NY crane bid: https://steubencountyny.gov/Archive.aspx?ADID=2773 [search excerpt only]
- WorkSafeBC, crane operator certification: https://www.worksafebc.com/en/health-safety/education-training-certification/crane-operator [search excerpt only]
- Ontario O. Reg. 88/13 (amending O. Reg. 213/91 s.150): https://www.ontario.ca/laws/regulation/r13088 [search excerpt only]

Health
- BC Pool Regulation, B.C. Reg. 296/2010 (current to 27 Oct 2026): https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/296_2010 [page opened]
- Halton Region, Pool and Spa Operator Guide (5 Sep 2025): https://www.halton.ca/Repository/Pool-Owner-Operator-Information-Package [page opened]
- Simcoe Muskoka District Health Unit, Reg. 565 amendments letter (28 Jan 2025): https://www.simcoemuskokahealth.org/docs/default-source/topic-safewater/2024-reg-565-amendments-final.pdf [page opened]
- Ontario O. Reg. 502/24 (Public Pools amendment): https://www.ontario.ca/laws/regulation/r24502 [search excerpt only]
- R.R.O. 1990, Reg. 565 Public Pools, consolidated (s.2, s.5, s.7(8), s.26.0.1 read): https://www.ontario.ca/laws/regulation/900565 [regulation text read, fact-check 2026-11-01]
- NCCEH, rapid review on saunas (2026): https://ncceh.ca/resources/evidence-briefs/rapid-review-environmental-health-risks-and-safety-considerations-saunas [search excerpt only; 403]
- Vancouver council motion on saunas and cold plunges (Jun 2024): https://council.vancouver.ca/20240626/documents/cfscA3.pdf [search excerpt only; 403]
- CBC, Vancouver saunas and cold plunges: https://amp.cbc.ca/news/canada/british-columbia/hot-saunas-cold-plunges-1.7246528 [search excerpt only]
