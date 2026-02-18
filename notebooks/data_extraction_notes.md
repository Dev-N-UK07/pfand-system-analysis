# Data Extraction Notes — Pfand System Analysis

## 1. Overview

This file tracks which tables I will extract from each PDF, and any issues or assumptions during extraction.

## 2. Sources and Planned Tables

### 2.1 UBA_2022_MAIN (data/raw/uba/uba_156_2024.pdf)

This dataset provides the official 2022 tonnage, recycling rates, and material flows for Germany’s deposit-bearing beverage packaging system, forming the core of your analytical and ESG modeling work.

#### UBA_2022 — Key Tables Identified (Pfand Relevant)

1. Tabelle 90 — Aufkommen von Verpackungen nach VerpackG 2022 (in kt)
   Page: 278
   Use: CORE (Pfand material input volumes)
   Notes: Column "Verpackungen gemäß § 31 VerpackG" gives Pfandpflichtige volumes.

   Extraction Status — Tabelle 90 (Completed)
   Source: Tabelle 90 — Aufkommen von Verpackungen nach VerpackG 2022 (UBA Texte 156/2024, page 278)
   Method: Manual extraction
   Output file: data/cleaned/uba_2022_table90.csv
   Units: kt (kilotonnes)
   Transformations:
   Decimal commas → decimal points
   “-” converted to blank values
   Removed aggregate “Summen” rows
   Retained only material categories relevant for Pfand analysis (rows 1–6)
   Quality notes:
   Cross-checked all numeric entries with table screenshot
   Verified §31 column as Pfand-specific
   No mismatches detected

2. Tabelle 99 — Stoffliche Verwertung von Verpackungen nach § 31 VerpackG 2022 (in kt)
   Page: 287
   Use: CORE (Pfand recycling output volumes)
   Notes: Required for material flow comparison.

    Extraction Status — Tabelle 99 (Completed).
    Source: Tabelle 99 — Stoffliche Verwertung nach § 31 VerpackG 2022 (UBA Texte 156/2024, page 287)
    Method: Manual extraction
    Output file: data/cleaned/uba_2022_table99.csv
    Units: kt (kilotonnes)
    Transformations:
    Decimal commas → decimal points
    “–” converted to blank cells
    Removed “Summen” rows
    Only materials 1–6 extracted (Pfand-relevant)
    Quality notes:
    Verified Verpackungsverbrauch column matches Table 90 §31 values
    Werkstoffliche & Stoffliche Verwertung totals checked
    No inconsistencies detected

3. Tabelle 100 — Stoffliche Verwertung von Verpackungen nach § 31 VerpackG 2022 (in %)
   Page: 288
   Use: CORE (Recycling rates)
   Notes: Key ESG indicator.

    Extraction Status — Tabelle 100 (Completed)
    Source: Tabelle 100 — Stoffliche Verwertung nach § 31 VerpackG 2022 (UBA Texte 156/2024, page 288)
    Method: Manual extraction
    Output file: data/cleaned/uba_2022_table100.csv
    Units: Percent (%) and kilotonnes (kt)
    Transformations:
    Decimal commas → decimal points
    “–” converted to blank
    Included “Verpackungsverbrauch” column to preserve completeness
    Removed Summen rows
    Quality notes:
    Checked percent values against Table 99 ratios
    No inconsistencies detected
    Material categories aligned with Tables 90 and 99


#### Master Dataset — pfand_2022_master.csv Created
Merged Table 90 (input), Table 99 (output), and Table 100 (rates)
Includes rows 1–6 (Pfand-relevant)
Empty values preserved for non-applicable materials
Will be used for:
EDA
ESG modeling
Flow analysis
Dashboards

#### Optional but Good for EDA / Storytelling

4. Tabelle 3 — Entwicklung des Verpackungsverbrauchs 2010–2022
   Page: 54

5. Tabelle 54 — Entwicklung der Verwertungsquote 2010–2022
   Page: 176

6. Tabelle 63 — Entwicklung des Verpackungsverbrauchs (neue Methode)
   Page: 198

7. Tabelle 85 — Mehrwegquote (2019–2021)
   Page: 254

### 2.2 UBA_2020_MAIN (data/raw/uba/uba_109_2022.pdf)

This dataset contains the official 2020 Pfand tonnage and recycling performance, enabling historical comparison and validation across multiple years.

#### UBA_109_2022 — Key Tables Identified (For 2020 & Historical Context)

#### CORE TABLES (Pfand System Data for 2020)

1.  Table 79 — Aufkommen von Verpackungen nach VerpackG 2020 (in kt)
    Page: 242
    Use: CORE – Pfand input volume (Glass, Metal, PET)
    Notes: Equivalent of Table 90 in 2022 report. Contains column “Verpackungen gemäß § 31 VerpackG”.

2.  Table 88 — Stoffliche Verwertung von Verpackungen nach § 31 VerpackG 2020 (in kt)
    Page: 251
    Use: CORE – Pfand recycling output (tonnes).

3.  Table 89 — Stoffliche Verwertung von Verpackungen nach § 31 VerpackG 2020 (in %)
    Page: 252
    Use: CORE – Pfand-specific recycling rate (%).

#### OPTIONAL TABLES (Trend / Narrative / EDA)

4.  Table 3 — Entwicklung des Verpackungsverbrauchs 2010–2020
    Page: 50
    Use: Long-term packaging trends (Glass, Plastic, Paper, Metal).

5.  Table 4 — Entwicklung des Verpackungsverbrauchs 1991–2020
    Page: 51
    Use: Deep historical context.

6.  Table 74 — Verbrauchsdaten von wiederverwendbaren Verpackungen (Mehrwegquote)
    Page: 220
    Use: Reusable share (Mehrwegquote), especially for beverage plastics.

7.  Table 46 — Entwicklung der Quoten der werkstofflichen Verwertung
    Page: 148
    Use: General recycling trends (not Pfand-specific).

### 2.3 UBA_LCA_2024 (data/raw/lca/uba_124_2024_lca.pdf)

This report supplies the CO₂ impact values, functional unit definitions, and packaging specifications needed to convert Pfand material volumes into environmental impact metrics.

#### UBA_124_2024_LCA — Key Tables & Data (For Phase 3 ESG Modeling)

1.  Functional Unit (CORE)
    Source: Chapter 3.2.2.1
    Functional Unit = Provision of 1000 L of beverage in packaging up to 10 L at Point-of-Sale.
    All CO₂ values in the impact tables are expressed per 1000 L functional unit.

2.  Climate Impact Tables (“Klimawandel”) — CORE
    We will extract the following absolute climate impact values (kg CO₂-eq per FU):
    PET Single-Use Bottle
    Approx. 87.58 kg CO₂-eq / FU
    Table: PET impact (Annex section)  
    Aluminium Beverage Can
    Approx. 248.66 kg CO₂-eq / FU
    Table: Aluminium Can impact (Annex section)
    Glass Reusable Bottle
    Approx. 39.94 kg CO₂-eq / FU
    Table: Glass Reusable (Annex section)
    These values represent the baseline carbon footprint for each system.

3.  Packaging Weights — CORE  
    (To convert CO₂ per FU → per bottle → per kg material)
    From material specification section (pg 231–232):
    PET 0.5 L: ~20.5 g
    PET 1.5 L: ~34.9 g
    Aluminium 0.33 L can: ~12–14 g
    Glass 0.5–1.0 L: 350–550 g (system-specific)
    We will use representative weights based on the system we model (PET, Alu, Glass).

4.  Recycling / Disposal CO₂ (“Recycling/Entsorgung”) — OPTIONAL
    These tables give:
    CO₂ burden from disposal
    CO₂ credit from recycling
    Used to enhance Phase 3 ESG storytelling.

5.  Transport Distance Assumptions — OPTIONAL
    Located in contextual discussion (summary text).
    Helpful for narrative, not extracted numerically.

### 2.4 Industry & Supporting Sources

This industry report provides verified global return-rate benchmarks that contextualize Germany’s 98% Pfand performance against other top-performing deposit systems worldwide.

## TOMRA_deposit_rate.pdf — Key Tables & Data (Step 2)

1.  Global High-Performing Return Rates (CORE)
    Source: Figure 12 (Return rates and deposit values for top-performing DRS)  
    Countries and return rates:

    - Finland: 99%
    - Germany: 98%
    - Denmark: 93%
    - Norway: 92%
    - Lithuania: 90%
    - Slovakia: 90%
    - Estonia: 89%
    - Iceland: 89%
      Use:
    - Benchmark chart in Phase 2
    - Validates that Germany operates at world-class efficiency

2.  Return-to-Retail Model Performance (CORE for Narrative)
    Source: Figure 15 (Container return rates for best-practice return-to-retail systems)

    - Germany ~98%
    - Finland >98%
    - Denmark ~93%
    - Norway ~92%
      Use:
    - Explains why Germany’s Pfand system achieves ~98% return rate
    - Supports narrative: retail participation drives high performance

3.  Redemption Network Density (OPTIONAL but impactful)

    - Norway: 1 redemption point per 366 people (explicit)
    - Germany: ~1 per 600–650 people (from TOMRA infographic; narrative only)
      Use:
    - Strong contextual metric for dashboard story

4.  Deposit Value Comparison (OPTIONAL)

    - Germany: €0.25
      Use:
    - Explains incentive strength behind high return rates

5.  Exclusions
    Do NOT extract:
    - Handling fee details
    - CSA cost/revenue tables
    - U.S. case studies
    - Text-heavy descriptions
    - RVM technical notes
      These are irrelevant to the Pfand analytics workflow.

## TOMRA Whitepaper (Unlocking Circularity) — Key Insights Identified (Step 2)

This whitepaper provides the conceptual framework and system-design insights that explain why high-performing deposit systems (like Germany’s Pfand) enable closed-loop recycling and strong circular economy outcomes.
Purpose:

- Narrative and conceptual source explaining why deposit-return systems enable high-quality, closed-loop recycling.
  Key Insights to Extract:

1. Circular Economy Framework (CORE narrative)
   - TOMRA’s Collect → Sort → Recycle model.
   - Shows how Pfand systems create clean, high-quality material streams.
2. System Design Principles (Supports Benchmarking)
   - Highlights benefits of return-to-retail systems, high deposit values, and automated collection.
   - Aligns with Germany’s decentralized retail-based Pfand structure.
3. Closed-Loop PET Recycling Logic
   - Illustrations and explanations of how deposit systems allow bottle-to-bottle recycling.
   - Supports your ESG modeling narrative (higher return = higher CO₂ savings).
4. Quality of Material Streams
   - Emphasizes reduced contamination and higher-value recycling outputs from Pfand-type systems.
     Usage in Project:

- Context and narrative (README, dashboard text, project introduction).
- Supportive evidence for system design comparisons (with TOMRA deposit-rate + Reloop data).
- Strengthens “Why Germany’s Pfand works” story.
  Exclusions:
- No numeric tables required for extraction (document is conceptual).
- No direct data modeling use; purely narrative + system logic.

## Reloop_Deposit_Book.pdf — Key Data Identified (Step 2)

## Reloop Deposit Book — Germany Profile (Validated)

This report offers country profiles, governance models, flow-of-funds insights, and global performance comparisons, including Germany’s system design, return rate, and economic structure.

1. Return Rate (CORE)

- Germany: 98% return rate for one-way beverage containers (2023).

2. Deposit Value

- €0.25 per container (standardized across PET, cans, glass).

3. System Type

- Decentralized, Retail-managed system (Return-to-Retail model).
- Retailers operate and maintain RVMs and collection logistics.

4. Handling Fee (CRITICAL FINDING)

- Handling Fee: €0.00
- Quote: “Although retailers do not receive a handling fee, they own the collected material and are responsible for selling it.”
- Implication: Retailers earn revenue from selling collected PET/Alu/Glass scrap.

5. Unredeemed Deposits (URDs)

- URDs are kept within the industry (producers/retailers), not by government.
- Important for building the economic-flow model.

6. Economic Flow Implications (CORE)
   Retailer Revenue Model:
   Retailer_Revenue = Sum(Returned_Tonnage × Scrap_Value_per_Ton)
   Not based on handling fees.

7. Optional Narrative Data

- Germany was an early adopter of DRS (2003 + 2006 expansion).
- System design is strongly convenience-driven (“return-to-retail”).

## CPI_Germany.csv — Key Data Identified (Supporting Dataset)

This monthly Destatis dataset tracks Germany’s consumer price index, providing economic context for interpreting deposit values and material consumption trends over time.
Source: Destatis (Verbraucherpreisindex für Deutschland)
Format:

- Semicolon-delimited CSV from Destatis (requires `sep=";"` when loading).
- 72 rows x 18 columns (monthly CPI for Germany overall).
  Relevant columns:
- `time`: Year (e.g., 2020, 2021, 2022).
- `1_variable_attribute_label`: Month name (Januar–Dezember).
- `value`: CPI index value (string with comma decimal).
- `value_unit`: Typically “2020=100”.
  Planned use:
- Inflation context for narrative or deposit buying-power analysis.
- Optional: real-value adjustment of €0.25 deposit.

## Population_Germany.csv — Key Data Identified (Supporting Dataset)

This annual Destatis dataset records Germany’s population over time, enabling per-capita normalization of Pfand material volumes and strengthening trend analysis.
Source: Destatis population statistics for Germany.
Format:

- Semicolon-delimited CSV (loaded with `sep=";"`).
- 75 rows x 14 columns.
  Relevant columns:
- `time`: Year (string, later converted to int).
- `value`: Population count (int).
- `value_unit`: Unit of population (e.g., Personen / in 1000).
  Planned use:
- Create per-capita Pfand indicators:
  PET tonnes per person, Glass per person, etc.
- Strengthen EDA & storytelling.
  Phase 1 notes:
- Already structured; no extraction needed at this stage.
