import pandas as pd

def load_salm(filepath):
    """
    Load the SALM dataset from CSV file. """

    df = pd.read_csv(filepath, skiprows=2)
    return df
