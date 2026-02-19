from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

# Spatial resolution (Uber commonly uses 8–9)
H3_RESOLUTION = 8

# Time aggregation (minutes)
TIME_INTERVAL = "15min"

# NYC bounding box (rough)
NYC_BOUNDS = {
    "min_lat": 40.5,
    "max_lat": 40.95,
    "min_lon": -74.3,
    "max_lon": -73.6,
}
