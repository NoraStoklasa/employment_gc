def filter_sa2(df):
    """Filter the SALM SA2 dataset to include only records for the Gold Coast region."""
    filtered_df = df["SA2 Code (2021 ASGS)"].astype(str).str.startswith("309")
    return df[filtered_df]