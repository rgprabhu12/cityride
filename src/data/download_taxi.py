import os
import requests
from pathlib import Path
from tqdm import tqdm
from src.config import RAW_DIR

BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"

def download_yellow_taxi(year=2023, months=[1]):
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    for month in months:
        file_name = f"yellow_tripdata_{year}-{str(month).zfill(2)}.parquet"
        url = f"{BASE_URL}/{file_name}"
        output_path = RAW_DIR / file_name

        if output_path.exists():
            print(f"{file_name} already exists.")
            continue

        print(f"Downloading {file_name}...")
        response = requests.get(url, stream=True)

        with open(output_path, "wb") as f:
            for chunk in tqdm(response.iter_content(chunk_size=1024)):
                if chunk:
                    f.write(chunk)

        print(f"Saved to {output_path}")

if __name__ == "__main__":
    download_yellow_taxi(year=2023, months=[1,2,3])
