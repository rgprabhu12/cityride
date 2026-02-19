import pandas as pd
from src.config import PROCESSED_DIR

def add_time_features(df):
    df["hour"] = df["time_bin"].dt.hour
    df["day_of_week"] = df["time_bin"].dt.dayofweek
    df["is_weekend"] = df["day_of_week"].isin([5,6]).astype(int)
    return df

def add_lags(df):
    df = df.sort_values(["h3_id", "time_bin"])
    df["lag_1"] = df.groupby("h3_id")["demand"].shift(1)
    df["lag_4"] = df.groupby("h3_id")["demand"].shift(4)
    return df

def build_model_dataset():
    df = pd.read_parquet(PROCESSED_DIR / "hex_demand.parquet")
    df = add_time_features(df)
    df = add_lags(df)
    df = df.dropna()

    df.to_parquet(PROCESSED_DIR / "model_dataset.parquet")
    print("Model dataset ready.")

if __name__ == "__main__":
    build_model_dataset()
