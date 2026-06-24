import pandas as pd

def reshape_salm(df):
    """Reshape SALM data from wide format to long format, with one row per SA2 and quarter."""
    melted_df = df.melt(
        id_vars=['Data Item', 'Statistical Area Level 2 (SA2) (2021 ASGS)', 'SA2 Code (2021 ASGS)'],
        var_name='Quarter',
        value_name='Value'
    )
    return melted_df