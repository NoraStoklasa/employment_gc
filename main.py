import pandas as pd

from src.ingest.load_salm import load_salm
from src.ingest.filter_sa2 import filter_sa2
from src.ingest.filter_lga import filter_lga
from src.ingest.reshape import reshape_salm
from src.ingest.combine import combine


def main():

    # SA2 pipeline
    sa2_df = load_salm("data/raw/SALM Smoothed SA2 Datafiles (ASGS 2021) - December quarter 2025.csv")
    filtered_sa2 = filter_sa2(sa2_df)
    reshaped_sa2 = reshape_salm(filtered_sa2)

    # LGA pipeline
    lga_df = load_salm("data/raw/SALM Smoothed LGA Datafiles (ASGS 2025) - December quarter 2025.csv")
    filtered_lga = filter_lga(lga_df)
    reshaped_lga = reshape_salm(filtered_lga)

    # Combine SA2 and LGA datasets
    combined_df = combine(reshaped_sa2, reshaped_lga)

    combined_df.to_csv("data/processed/combined_salm_data.csv", index=False)



if __name__ == "__main__":
    main()
