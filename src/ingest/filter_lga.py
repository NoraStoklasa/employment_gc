CAPITAL_CODES = [
    "33430",  # Gold Coast
    "31000",  # Brisbane
    "17200",  # Sydney
    "24600",  # Melbourne
    "40070",  # Adelaide
    "57080",  # Perth
    "62810",  # Hobart
    "71000",  # Darwin
    "89399",  # Canberra (ACT)
]


def filter_lga(df):
    """Filter the LGA dataset to include only records for the capitals."""
    filtered_df = df["LGA Code (2025 ASGS)"].astype(str).isin(CAPITAL_CODES) | df["LGA Code (2025 ASGS)"].astype(str).str.startswith("3")
    return df[filtered_df]


