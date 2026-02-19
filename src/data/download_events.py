import requests
import pandas as pd
from src.config import RAW_DIR

def download_events(limit=5000):
    url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
    params = {"$limit": limit}

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data)
    df.to_parquet(RAW_DIR / "events_raw.parquet")

    print("Event data saved.")

if __name__ == "__main__":
    download_events()