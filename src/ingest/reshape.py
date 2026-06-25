import pandas as pd

def reshape_salm(df):
    """Reshape SALM data from wide format to long format, with one row per SA2 and quarter."""
    melted_df = df.melt(
        id_vars=['Data Item', 'Statistical Area Level 2 (SA2) (2021 ASGS)', 'SA2 Code (2021 ASGS)'], # Variables to keep as identifiers
        var_name='Quarter', # Name of the new column that will contain the quarter information
        value_name='Value' # Name of the new column that will contain the values
    )
    return melted_df