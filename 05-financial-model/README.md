# Vantage Sauna Co. financial model (Canada, C$)

`vantage-financial-model.xlsx` is the five-year model behind the base plan in `07-brief/BRIEF.md` §5 and the raise in `08-launch-plan/launch-plan.md`. It runs by quarter from Q1 2027 to Q4 2031. All figures are in Canadian dollars (C$), before GST/PST/HST. They are planning estimates, not forecasts of actual results.

The workbook reproduces the quarterly cash model that produced the plan. Every year and every quarter matches to within C$1.

## Key outputs (base case)

| C$ | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---|---|---|---|---|
| Installs (Vancouver / Victoria / Toronto) | 5 (4/1/0) | 14 (7/1/6) | 24 (9/2/13) | 34 (11/2/21) | 45 (13/3/29) |
| Installed base, year end | 5 | 19 | 43 | 77 | 122 |
| Total revenue | 782,680 | 2,529,508 | 4,659,967 | 6,761,349 | 9,158,533 |
| Gross profit | 149,022 | 855,474 | 1,856,562 | 2,818,395 | 3,853,288 |
| EBITDA | -902,619 | -319,682 | 153,725 | 688,436 | 1,326,633 |
| Net income before income tax | -931,176 | -252,838 | 77,970 | 627,148 | 1,258,047 |
| Cash at year end | 1,191,726 | 974,369 | 1,021,118 | 1,689,129 | 2,681,152 |

- **Lowest quarter-end cash: C$841,267 in Q2 2029**, with a C$2.0M seed in Q1 2027 and a C$350k CSBFP loan in Q2 2027.
- EBITDA turns positive in 2029.
- Sources and uses, 2027–2028: uses C$2,725,473; sources C$3,699,842 (seed 2,000,000; loan 350,000; gross profit from 19 installs 1,004,496; IRAP and SR&ED 227,963; customer deposits ahead of builds 117,383). That leaves C$974,369 at the end of 2028.

**Seed-size sensitivity (base case)**

| Seed | Lowest quarter-end cash | Quarter | Cash at end of 2031 | Months of that year's opex at the low point |
|---|---|---|---|---|
| None | -C$1,158,733 | Q2 2029 | C$681,152 | Runs out (below zero from Q1 2027) |
| C$1.5M | C$341,267 | Q2 2029 | C$2,181,152 | 2.4 |
| **C$2.0M** | **C$841,267** | **Q2 2029** | **C$2,681,152** | **5.9** |
| C$2.5M | C$1,341,267 | Q2 2029 | C$3,181,152 | 9.5 |

**Conservative case** (the research's 81 buildings; same costs and hires): revenue C$0.62M / 1.81M / 3.12M / 4.59M / 5.75M; EBITDA -C$0.93M / -0.54M / -0.42M / -0.16M / -0.01M (about break-even by 2031). With a C$2.0M seed, cash is C$0.15M at the end of 2029 and drops below zero in Q2 2030. It ends 2031 at -C$0.32M. That is why the brief says the 2029–2030 hires would be delayed in this case.

## Sheets

| Sheet | What it does |
|---|---|
| **README** | Purpose, live key results, how to use the model, colour legend, sheet map, method notes and sources. |
| **Assumptions** | Every input in one place, with a source note on each row. It holds the scenario switch, product prices, costs and mix, add-ons, the recurring plans and attach rates, pilot discounts and the learning curve, payment terms, both install plans, the hires, opex lines, capex items, the seed and loan, IRAP, SR&ED, the tax memo rates and the seed sizes to test. |
| **Unit Economics** | Per-model margins, the C$181,500 blended contract (42.2% gross margin at steady state) and C$10,048.50 of recurring revenue per building. It also gives the price and cost per install for each year (pilot discount, cost uplift, Toronto freight). |
| **Team** | Payroll by role and quarter (loaded salary x 1.03^(year − 2027) / 4 from the start quarter), headcount (4 / 6 / 8 / 10 / 11 at year end) and the yearly SR&ED claim. |
| **Quarterly Cash Flow** | The engine. For each of the 20 quarters it works out installs, installed base, revenue, cost of goods, opex and EBITDA. It then turns them into cash: 50% deposits a quarter ahead, 60% of build cost a quarter ahead, capex, IRAP, SR&ED, the loan schedule and the seed. It ends with closing cash and the lowest quarter-end cash. |
| **Annual P&L** | Yearly totals from the quarterly sheet, then depreciation, loan interest, IRAP and SR&ED, down to net income before income tax. It also has a memo tax estimate, year-end cash and the depreciation schedule. |
| **Funding** | Key results, the 2027–2028 sources and uses table (launch plan §1.3), and the seed-size sensitivity with a helper block of quarter-end cash for each seed size. |
| **Checks** | The base case against the cash model, year by year (tolerance C$2,000), plus integrity checks. It should show "Matches the base plan" and "All checks pass". |
| **Charts** | Quarter-end cash, revenue by line, and EBITDA with net income. |

## Inputs and formulas

- **Inputs** are blue text on a light-yellow fill, and they all sit on the Assumptions sheet. Edit only these.
- **Formulas** are black. **Links** to another sheet are green. **Key results** are bold on a light Ember tint. Notes and units are grey italic.
- Everything outside Assumptions is a live formula. The only exceptions are the colour-legend samples on the README sheet and the cash-model reference values on the Checks sheet.
- The file opens with full recalculation turned on (`fullCalcOnLoad`). Each formula cell also stores its last computed value, so previews and phone viewers show numbers too.

## How to switch scenarios

1. Open **Assumptions** and go to cell **C5**.
2. Pick **Base** (122 buildings by 2031) or **Conservative** (81 buildings) from the drop-down.
3. Every sheet follows. The active install plan is in Assumptions rows 63–71. The Checks sheet compares against the base plan only while C5 = Base.

Other levers:
- **Seed size used everywhere:** Assumptions C110 (amount), C111:C112 (year and quarter).
- **Seed sizes tested on the Funding sheet:** Assumptions C139:F139 (none, C$1.5M, C$2.0M, C$2.5M).
- **Install plans:** Assumptions rows 43–50 (base) and 53–60 (conservative). Keep each year's quarterly installs equal to its city total; the check rows (51 and 61) should read 0.

## Method and simplifications

1. Installs are whole buildings per quarter. Each install is priced at the year's contract value: C$181,500 less the pilot discount (15% in 2027, 5% in 2028). Its cost is C$104,912.50, plus the learning-curve uplift (20% / 8% / 3% in 2027–2029), plus C$7,500 freight times the year's Toronto share.
2. Customers pay 50% the quarter before install and 50% in the install quarter. Vantage pays 60% of build cost (materials) the quarter before install and 40% in the install quarter.
3. The model stops at Q4 2031. It books no deposits or materials for 2032 installs. That makes end-2031 cash about C$0.3M lower than a business still selling would show.
4. Care and Access bill from the middle of the install quarter: start-of-quarter base plus half of that quarter's installs.
5. Payroll covers non-COGS staff only; factory and install labour are in cost of goods. Salaries rise 3% a year. Opex lines are spread evenly over each year's quarters. Sales commission is 3% of hardware revenue.
6. Depreciation is straight line over 5 years, with a full year in the year of purchase.
7. IRAP (C$150k) and SR&ED refunds are other income in the quarter received. The SR&ED claim is 35% x 55% x (eligible engineering salaries + non-payroll engineering spend), refunded in Q3 of the next year. As in the cash model, an eligible engineer counts for the full year they start (the design engineer in 2029).
8. Net income is before income tax, as in the brief. Annual P&L rows 41–47 estimate tax after losses (11% on the first C$500k, 27% above): about C$130k in 2031. It is not deducted from cash.
9. The C$150k pre-seed (Nov 2026 to Mar 2027) sits outside the model, so opening cash on 1 Jan 2027 is C$0. Sales taxes pass through and are left out.
10. The CSBFP loan is drawn in Q2 2027. Interest is 7.45% a year on the balance after the draw. Principal is repaid at C$17,500 a quarter from Q1 2028, and C$70,000 is still owed at the end of 2031.

## Open items

- **Loan rate.** The model uses the cash-model rate of 7.45% (prime 4.45% + 3%). Banks raised prime to 4.70% on 29 Oct 2026, so the CSBFP maximum is now 7.70%, which matches the brief's wording. Entering 7.70% in Assumptions C116 has these effects: end-2031 cash falls by C$2,844, the low point falls by C$1,805 to C$839,462 (still Q2 2029), and net income changes by less than C$1,000 a year. No rounded figure in the brief changes. The quarterly cash table in launch plan §1.4 (in C$000) would move by 1–3 in some quarters.
- **SR&ED full-year salary.** Counting only the design engineer's three paid quarters in 2029 would lower the 2030 refund by about C$5.6k. The model keeps the cash-model method so that it matches the plan.

## How it was checked

The workbook was recalculated with the Python `formulas` engine (no spreadsheet app needed). The results were compared with the cash model, `cashmodel.py`, run on the base and conservative settings:
- 0 formula errors in 2,543 formula cells.
- Base case: revenue, gross profit, opex, payroll, EBITDA, depreciation, interest, IRAP, SR&ED, net income, capex and year-end cash for each year, all 20 quarter-end cash balances, the low point (C$841,267, Q2 2029), the four seed sizes and the 2027–2028 sources and uses all match within C$1.
- Conservative case: all of the same items match within C$1.

Sources: `07-brief/BRIEF.md` (v4), `08-launch-plan/launch-plan.md`, `06-research/canada-market-research.md`, `06-research/canada-competition-and-costs.md`, `06-research/canada-codes-and-engineering.md`.
