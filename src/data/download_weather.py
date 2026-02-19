import meteostat as ms
from datetime import datetime
import pandas as pd
from src.config import RAW_DIR

def download_weather():

    start = datetime(2023, 1, 1)
    end = datetime(2023, 12, 31)

    # NYC coordinates
    location = ms.Point(40.7128, -74.0060)

    # Explicitly find nearest station
    stations = ms.stations.nearby(location)
    print(stations)

    if stations is None:
        raise ValueError("No weather station found near NYC.")

    station_id = stations.index[0]
    print(f"Using station: {station_id}")

    data = ms.hourly(station_id, start, end)
    df = data.fetch()

    if df is None or df.empty:
        raise ValueError("Weather data fetch returned empty dataframe.")

    df = df.reset_index()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    df.to_parquet(RAW_DIR / "weather_2023.parquet")

    print("Weather data saved successfully.")

if __name__ == "__main__":
    download_weather()
