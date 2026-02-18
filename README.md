# Pfand System Analysis (Germany) — Deposit Return Scheme (ESG Data Analytics)

A portfolio-ready data analytics case study on Germany’s **Pfand (deposit-return)** system.
This project combines **macro packaging trends (2010–2022)** with a **Pfand 2022 baseline deep-dive** to quantify:
- operational performance (recycling efficiency),
- environmental impact (CO₂ avoided),
- financial mechanism (deposit circulation + unclaimed value),
- statutory validation (2020 vs 2022 audit checkpoint).

---

## Dashboard Preview

### Page 1 — The Macro Problem (2010–2022)
Germany’s packaging market scale and material mix evolution.

![Dashboard Page 1](assets/dashboard/page1_macro.png)

### Page 2 — The Pfand Solution & Impact (2022 Baseline)
Pfand system scale, CO₂ avoided by material, deposit money flow, and statutory audit checkpoint.

![Dashboard Page 2](assets/dashboard/page2_pfand_impact.png)

---

## Key Results (2022 Baseline)
- **Pfand input:** 549.3 kt  
- **Recycled:** 526.8 kt  
- **Avg recycling rate:** 97.9%  
- **CO₂ avoided:** ~0.99 Mt  
- **Deposit circulation:** ~€5.27bn  
- **Audit checkpoint:** official §31 tables show recycling-rate change (2020 → 2022, pp) by material

> Note: Results are based on Pfand-specific statutory reporting (§31 VerpackG) and a 2022 baseline deep-dive.

---

## Data Sources (Primary)
- Umweltbundesamt (UBA) reports / statutory tables:
  - UBA 156/2024 — §31 tables (2022)
  - UBA 109/2022 — §31 tables (2020)
- Additional industry references used for context (if applicable): TOMRA / Reloop (listed in `/sources` or notebook citations)

---

## Method (What I did)
- Extracted and cleaned official tabular data (Pfand-specific §31 tables + macro packaging trend tables)
- Built a modular transformation workflow in Python (pandas)
- Computed:
  - material-level volumes (kt)
  - recycling rate metrics
  - CO₂ avoided by material (using factor constants)
  - deposit value circulation and unclaimed Pfand (financial flow)
  - 2020 vs 2022 checkpoint deltas (pp)
- Delivered an interactive Power BI report with a consultant-style narrative:
  **Macro problem → Micro solution → Verified impact**

---

## Tech Stack
- Python (pandas, numpy)
- Jupyter Notebook
- Power BI (data model, measures, report pages)
- Git/GitHub

---

## Repository Structure
```text
data/
  raw/              # original source files (optional / not always committed)
  cleaned/          # dashboard-ready CSV outputs
notebooks/          # analysis notebooks
assets/
  dashboard/        # dashboard screenshots
  notebooks/        # notebook screenshots
dashboard/          # Power BI .pbix
