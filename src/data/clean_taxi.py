import pandas as pd
from src.config import RAW_DIR, INTERIM_DIR, NYC_BOUNDS

def clean_taxi(file_name):
    df = pd.read_parquet(RAW_DIR / file_name)

    # Standardize columns
    df = df.rename(columns={
        "tpep_pickup_datetime": "pickup_datetime",
        "tpep_dropoff_datetime": "dropoff_datetime"
    })

    # Drop invalid coordinates
    df = df[
        (df["pickup_latitude"].between(NYC_BOUNDS["min_lat"], NYC_BOUNDS["max_lat"])) &
        (df["pickup_longitude"].between(NYC_BOUNDS["min_lon"], NYC_BOUNDS["max_lon"]))
    ]

    # Trip duration
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
    df["dropoff_datetime"] = pd.to_datetime(df["dropoff_datetime"])

    df["trip_duration_min"] = (
        df["dropoff_datetime"] - df["pickup_datetime"]
    ).dt.total_seconds() / 60

    df = df[df["trip_duration_min"] > 0]

    INTERIM_DIR.mkdir(parents=True, exist_ok=True)
    output_file = INTERIM_DIR / f"cleaned_{file_name}"
    df.to_parquet(output_file)

    print(f"Saved cleaned file to {output_file}")

if __name__ == "__main__":
    clean_taxi("yellow_tripdata_2023-01.parquet")
