import pandas as pd

def reshape_salm(df):
    """Reshape SALM data from wide format to long format, with one row per SA2 and quarter."""
    melted_df = df.melt(
        id_vars=df.columns[:3].tolist(), # Variables to keep as identifiers
        var_name='Quarter', # Name of the new column that will contain the quarter information
        value_name='Value' # Name of the new column that will contain the values
    )
    melted_df.columns = ["metric", "region_name", "region_code", "quarter", "value"]
    return melted_df