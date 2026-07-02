"""
geocode_sa2.py

Reads unique SA2 suburb names from processed data, geocodes them using
OpenStreetMap Nominatim, and saves the results as a dbt seed CSV.

Run from the project root:
    python src/ingest/geocode_sa2.py
"""

import csv
import time
import requests
import pandas as pd
from pathlib import Path

INPUT = Path("data/processed/combined_salm_data.csv")
OUTPUT = Path("dbt/gold_coast_labour_market/seeds/gold_coast_sa2_lookup.csv")

HEADERS = {"User-Agent": "gold-coast-labour-market-pipeline (student project)"}


def geocode(region_name: str):
    """Look up lat/long for a Gold Coast suburb using Nominatim.
    Falls back to searching just the first part of the name if the full name fails.
    """
    url = "https://nominatim.openstreetmap.org/search"

    import re
    queries = [region_name]
    if " - " in region_name:
        parts = [p.strip() for p in region_name.split(" - ")]
        # Try each part, with brackets stripped e.g. "Ormeau (East)" -> "Ormeau"
        for part in parts:
            queries.append(part)
            queries.append(re.sub(r"\s*\(.*?\)", "", part).strip())

    for query in queries:
        full_query = f"{query}, Gold Coast, Queensland, Australia"
        params = {"q": full_query, "format": "json", "limit": 1}
        try:
            response = requests.get(url, params=params, headers=HEADERS, timeout=10)
            results = response.json()
            if results:
                return float(results[0]["lat"]), float(results[0]["lon"])
        except Exception as e:
            print(f"  Error geocoding {region_name}: {e}")
        time.sleep(1)

    return None, None


def main():
    df = pd.read_csv(INPUT)

    # Only geocode SA2 (Gold Coast suburbs), not LGAs
    sa2_df = df[df["level"] == "sa2"][["region_name", "region_code"]].drop_duplicates()
    sa2_df = sa2_df.sort_values("region_name").reset_index(drop=True)

    print(f"Geocoding {len(sa2_df)} SA2 suburbs...")

    results = []
    for _, row in sa2_df.iterrows():
        name = row["region_name"]
        code = row["region_code"]
        print(f"  {name}...", end=" ")
        lat, lon = geocode(name)
        print(f"{lat}, {lon}")
        results.append({"region_code": code, "region_name": name, "latitude": lat, "longitude": lon})
        time.sleep(1)  # Nominatim rate limit: 1 request per second

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(results).to_csv(OUTPUT, index=False)
    print(f"\nSaved to {OUTPUT}")

    # Print any that failed
    failed = [r["region_name"] for r in results if r["latitude"] is None]
    if failed:
        print(f"\nFailed to geocode ({len(failed)}):")
        for name in failed:
            print(f"  {name}")


if __name__ == "__main__":
    main()
