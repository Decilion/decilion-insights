#!/usr/bin/env python3
"""
Recompute the report's signature value-vs-mass figures from the published raw data.

Uses only the Python standard library (no pandas, no installs). From this folder:

    python3 reproduce.py

Source: "Made in the Region, Up to a Point: Pharmaceutical Supply Security in Latin
America and the Caribbean" (Decilion Insights, 2026).
https://decilion.com/insights/drug-manufacturing-lac/
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "clean", "volume_vs_value_kg_2024.csv")

t = {k: 0.0 for k in ("imp_usd", "extra_usd", "intra_usd",
                      "total_kg", "extra_kg", "intra_kg")}
n = 0
with open(CSV, newline="") as f:
    for row in csv.DictReader(f):
        for k in t:
            t[k] += float(row[k])
        n += 1

val_share = t["extra_usd"] / t["imp_usd"]
mass_share = t["extra_kg"] / t["total_kg"]
uv_extra = t["extra_usd"] / t["extra_kg"]
uv_intra = t["intra_usd"] / t["intra_kg"]

print(f"Markets aggregated:            {n} (the 10 largest, ~80% of LAC import value)")
print(f"Extra-regional VALUE share:    {val_share:.1%}   (report: ~91%)")
print(f"Extra-regional MASS share:     {mass_share:.1%}   (report: ~53%)")
print(f"Unit value, extra-regional:    US${uv_extra:,.0f}/kg   (report: ~US$103/kg)")
print(f"Unit value, intra-regional:    US${uv_intra:,.1f}/kg    (report: ~US$12/kg)")
print(f"Price-density ratio:           {uv_extra / uv_intra:.1f}x")
print()
print("The region imports a small tonnage of very expensive (extra-regional) medicine")
print("and a large tonnage of cheap (intra-regional) generics: it already makes the")
print("volume; what it imports is the value.")
