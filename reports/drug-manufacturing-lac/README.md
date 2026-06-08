# Made in the Region, Up to a Point — verify the headline

The calculation behind the signature finding of the Decilion report *[Made in the Region, Up to a Point: Pharmaceutical Supply Security in Latin America and the Caribbean](https://decilion.com/insights/drug-manufacturing-lac/)* (Decilion Insights, 2026).

> **Suggested citation:** García Ruiz, J. (2026). *Made in the Region, Up to a Point: Pharmaceutical Supply Security in Latin America and the Caribbean.* Decilion Insights. https://decilion.com/insights/drug-manufacturing-lac/

## Verify it yourself (no dependencies)

```bash
python3 reproduce.py
```

Recomputes the report's value-vs-mass result straight from the trade table, using only the Python standard library. Expected output: **~90.9% extra-regional by value, ~53.0% by mass, US$103/kg vs US$11.6/kg.** In other words, Latin America and the Caribbean imports most of its medicine *value* from outside the region but already makes most of its *volume* — the gap is in the high-value, patented slice.

`data/clean/volume_vs_value_kg_2024.csv` is the input: extra- and intra-regional import value (USD) and net mass (kg) for the ten largest LAC markets, which together hold about 80% of regional import value (2024 UN Comtrade, HS chapter 30).

## Want the full picture?

The complete country-level datasets, the manufacturing-capability typology, the active-ingredient (API) analysis, and the 2035 scenario models behind the report are part of Decilion's consulting work. For the full data, a custom analysis, or a briefing for your team, get in touch: **j.garcia@decilion.com**.

## License & contact

Script: MIT. Data table: CC BY 4.0. Corrections or suggestions: open an issue or email **j.garcia@decilion.com**.
