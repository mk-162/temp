# GTSE US Entry Research Plan

## 1. Baseline Analysis: gtse.co.uk
- **Value Prop:** UK's Most Trusted Consumables Supplier.
- **Key Categories:** Cable ties (Nylon, Stainless, etc.), Tape, Tools, Aerosols, Gloves.
- **B2B Signals:** "Trade Enquiries" button, "Trade accounts available for bulk purchases", "Bulk Box Deals".
- **UX:** Clear, category-driven, focuses on "Best Sellers" and bulk options.

## 2. Research Objectives
The primary goal is to map the US landscape for "Cable Ties" and related industrial consumables to inform GTSE's market entry.
1.  **Pricing Benchmark:** Determine the "street price" for key SKUs (e.g., 8" Black Nylon Cable Tie, 100pk & 1000pk) across different competitor types.
2.  **Logistics Standards:** Identify the expected shipping speeds, free shipping thresholds, and carrier choices.
3.  **UX/Trust Signals:** Analyze how US competitors build trust (e.g., certifications, detailed specs, reviews).
4.  **Product Assortment:** Map the depth and breadth of competitor catalogs (Do they sell just ties, or tools/tape too?).

## 3. Priority Competitors
Derived from `US Competitors .xlsx` and initial scoping.

| Tier | Competitor | Type | Key Focus |
| :--- | :--- | :--- | :--- |
| **Tier 1 (Direct)** | **Cable Ties Unlimited** | Specialist | Broad range, custom printing, strong SEO. |
| | **ZipTie.com** | Specialist | Retail-friendly, private label focus. |
| **Tier 2 (Broad)** | **Uline** | Industrial Giant | The benchmark for logistics and reliability. |
| | **Cable Ties & More** | Retail | niche cable management products. |
| **Tier 3 (Niche)** | **Cable Ties Plus** | Distributor | Nelco subsidiary, pure-play distribution. |
| | **BuyCableTies.com** | Discount | Price fighter (check for bottom-of-barrel pricing). |

## 4. Methodology
We will use a hybrid approach to gather data.

### A. Automated Data Collection (Scraping)
*Tools:* Python (`requests`, `BeautifulSoup`)
*Targets:*
-   **Product Data:** Title, Price, SKU, Quantity per Pack, "In Stock" status.
-   **Category Structure:** How they organize their hierarchy (e.g., by Material vs. by Size).
-   **Metadata:** SEO titles and descriptions to understand their keyword targeting.

### B. Manual Analysis (Qualitative)
*Focus:*
-   **Checkout Experience:** Simulate cart addition to check shipping costs and tax handling.
-   **Customer Service:** Test chat bots or support response times (if applicable).
-   **Content Quality:** Review product descriptions, datasheet availability, and video content.

## 5. Execution Plan

### Phase 1: Setup & Discovery (Current)
- [x] Identify key competitors.
- [x] Establish file structure.
- [x] Initial scrape of Uline (Complete).

### Phase 2: Deep Dive Data Collection
- [x] **Scrape Execution:** Run `scrape_competitors.py` (enhanced) against Tier 1 & 2 targets.
- [x] **Manual Audit:** Complete `dossier.md` for *Cable Ties Unlimited* and *ZipTie.com*.
- [x] **Pricing Matrix:** Populate `research/synthesis/matrix.md` with hard numbers for 5 core SKUs.

### Phase 3: Extended Competitor Analysis
- [x] **Scrape Expansion:** Update and run `scrape_competitors.py` for *Cable Ties & More* and *Cable Ties Plus*.
- [x] **Manufacturer Review:** Create aggregated dossier for *Panduit* and *HellermannTyton* (focus on positioning, not scraping).
- [x] **Dossier Creation:**
    -   `research/competitors/cable-ties-and-more/dossier.md` (Complete)
    -   `research/competitors/cable-ties-plus/dossier.md` (Complete)
    -   `research/competitors/manufacturers/dossier.md` (Complete)
- [x] **Matrix Update:** Integrate all new findings into the master matrix.

### Phase 4: Synthesis & Strategy
- [x] **Gap Analysis:** Compare GTSE UK's offering against US data.
- [x] **Logistics Strategy:** Draft recommendation for 3PL vs. direct shipping based on competitor standards.
- [x] **Final Report:** Compile all findings into `research/synthesis/entry_strategy.md`.

## Project Status: Complete
All research phases have been executed. The final strategy is available in `research/synthesis/entry_strategy.md`.

## 6. Gap Analysis (Missing Information)
*Data we need to actively hunt for:*
-   **Shipping Tiers:** Exact cost for "Next Day" vs "Ground" for a standard 5lb box.
-   **Return Policies:** Who pays for return shipping? (Critical for trust).
-   **Volume Discounts:** Are they public (tiered pricing tables) or hidden behind "Call for Quote"?
-   **Manufacturing Origins:** Do they explicitly state "Made in USA" vs "Imported"? (Patriotism can be a sales factor).

## 7. File Structure
The research directory is organized to support this plan:

```
research/
├── competitors/
│   ├── general_data/           # Broad market scrapes (JSON)
│   ├── uline/                  # Deep dive: Uline
│   ├── cable-ties-unlimited/   # Deep dive: CTU
│   │   ├── dossier.md
│   │   └── evidence/
│   └── ziptie-com/             # Deep dive: ZipTie.com
├── synthesis/
│   ├── matrix.md               # Pricing and feature comparison tables
│   ├── market_map.md           # Visualizing the competitive landscape
│   └── entry_strategy.md       # Final strategic recommendations
└── plan.md                     # This roadmap
```
