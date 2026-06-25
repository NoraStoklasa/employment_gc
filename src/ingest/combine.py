import pandas as pd

def combine(sa2_df, lga_df):
    """Combine SA2 and LGA datasets."""
    sa2_df["level"] = "sa2"
    lga_df["level"] = "lga"
    combined_df = pd.concat([sa2_df, lga_df]).reset_index(drop=True)
    return combined_df

if __name__ == "__main__":
    from load_salm import load_salm
    from filter_gold_coast import filter_gold_coast
    from filter_lga import filter_lga_capitals
    from reshape import reshape_salm

    sa2_raw = load_salm("data/raw/SALM Smoothed SA2 Datafiles (ASGS 2021) - December quarter 2025.csv")
    sa2_filtered = filter_gold_coast(sa2_raw)
    sa2_long = reshape_salm(sa2_filtered)

    lga_raw = load_salm("data/raw/SALM Smoothed LGA Datafiles (ASGS 2025) - December quarter 2025.csv")
    lga_filtered = filter_lga_capitals(lga_raw)
    lga_filtered = lga_filtered.rename(columns={
        "Local Government Area (LGA) (2025 ASGS)": "Statistical Area Level 2 (SA2) (2021 ASGS)",
        "LGA Code (2025 ASGS)": "SA2 Code (2021 ASGS)"
    })
    lga_long = reshape_salm(lga_filtered)

    result = combine(sa2_long, lga_long)
    print(result.shape)
    print(result["level"].value_counts())