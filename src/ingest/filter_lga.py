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

GOLD_COAST_CODES = [
    "33430",  # Gold Coast
]


def filter_lga_gold_coast(df):
    """Filter the LGA dataset to include only records for the Gold Coast region."""
    filtered_df = df["LGA Code (2025 ASGS)"].astype(str).isin(GOLD_COAST_CODES)
    return df[filtered_df]


def filter_lga_queensland(df):
    """Filter the LGA dataset to include only records for Queensland."""
    filtered_df = df["LGA Code (2025 ASGS)"].astype(str).str.startswith("3")
    return df[filtered_df]


def filter_lga_capitals(df):
    """Filter the LGA dataset to include only records for the capitals."""
    filtered_df = df["LGA Code (2025 ASGS)"].astype(str).isin(CAPITAL_CODES)
    return df[filtered_df]


