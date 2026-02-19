import pandas as pd
from src.config import INTERIM_DIR, PROCESSED_DIR, TIME_INTERVAL
from src.spatial.h3_utils import latlon_to_h3

def build_hex_demand(file_name):
    df = pd.read_parquet(INTERIM_DIR / file_name)

    df["h3_id"] = df.apply(
        lambda row: latlon_to_h3(
            row["pickup_latitude"],
            row["pickup_longitude"]
        ),
        axis=1
    )

    df["time_bin"] = df["pickup_datetime"].dt.floor(TIME_INTERVAL)

    agg = (
        df.groupby(["h3_id", "time_bin"])
        .size()
        .reset_index(name="demand")
    )

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    agg.to_parquet(PROCESSED_DIR / "hex_demand.parquet")

    print("Hex demand file created.")

if __name__ == "__main__":
    build_hex_demand("cleaned_yellow_tripdata_2023-01.parquet")
