import pandas as pd

def combine(sa2_df, lga_df):
    """Combine SA2 and LGA datasets."""
    sa2_df["level"] = "sa2"
    lga_df["level"] = "lga"
    combined_df = pd.concat([sa2_df, lga_df]).reset_index(drop=True)
    return combined_df
