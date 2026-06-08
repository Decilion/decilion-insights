# Made in the Region, Up to a Point — Data & Code

Reproducibility bundle for the Decilion report *[Made in the Region, Up to a Point: Pharmaceutical Supply Security in Latin America and the Caribbean](https://decilion.com/insights/drug-manufacturing-lac/)* (Decilion Insights, 2026).

> **Suggested citation:** García Ruiz, J. (2026). *Made in the Region, Up to a Point: Pharmaceutical Supply Security in Latin America and the Caribbean.* Decilion Insights. https://decilion.com/insights/drug-manufacturing-lac/

## Reproduce the signature finding (no dependencies)

```bash
python3 reproduce.py
```

Recomputes the value-vs-mass figures straight from the raw bilateral trade data, using only the Python standard library. Expected output: ~90.9% extra-regional by value, ~53.0% by mass, US$103/kg vs US$11.6/kg.

## Where each headline number comes from

| Claim in the report | File |
|---|---|
| ~91% of import **value** is extra-regional; ~53% of **mass**; US$103 vs ~US$12/kg | `data/clean/volume_vs_value_kg_2024.csv` (per-market; `reproduce.py` recomputes it) |
| ~US$33bn/yr of supply sourced outside the region (bottom-up, lower bound) | `data/clean/dependency_allpartner_2024.csv` |
| ~59% of active ingredients from China + India | `data/clean/api_dependence_efpia.csv` (EFPIA HS6 basket in `api_codes_efpia.csv`) |
| Capability typology: Dominican Republic the only RCA ≥ 1; four export-oriented formulators | `analysis/outputs/typology.csv` |
| RCA vintage robustness (2024 vs 2023, archetypes stable) | `analysis/outputs/capability_rca_robustness.csv` |
| Five non-reporters add ~US$0.3bn (mirror floor) | `data/clean/nonreporter_mirror.csv` |
| Cost-of-inaction scenarios to 2035 (19–32 points repatriable) | `analysis/outputs/scenarios.csv` |
| Data coverage across the LAC-33 | `data/outputs/coverage_matrix.csv` |
| Exhibit data (EX1–EX4) | `data/outputs/EX*.csv` |

## Method, in brief

Trade figures come from UN Comtrade: HS chapter 30 (finished medicines) and HS 2933/2937 plus the EFPIA basket (active ingredients), for the latest complete year (2024; 2023 where 2024 is incomplete). Extra-regional dependence is summed across **every** LAC partner (an all-partner method, not a top-handful approximation), by both value and net mass. The ~US$33bn headline is built **bottom-up**: the ten largest markets (~80% of regional import value) measured directly, plus conservative shares for the smaller reporters, treated as a **lower bound**. Full detail: [`methodology.md`](methodology.md) and the methodology section of the report.

## Caveats (stated in full in the report)

Trade is not production; net mass is a proxy for physical volume, not doses; the EFPIA API basket includes some non-pharmaceutical uses of the same tariff headings; the 2035 scenarios are a transparent bounded model, not a forecast.

## Questions, corrections, improvements

Open an issue, or email **j.garcia@decilion.com**. Released under CC BY 4.0.
