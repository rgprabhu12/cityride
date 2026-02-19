import h3
from src.config import H3_RESOLUTION

def latlon_to_h3(lat, lon):
    return h3.geo_to_h3(lat, lon, H3_RESOLUTION)
