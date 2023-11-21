from geopy.geocoders import GoogleV3
from app.config.config import GOOGLE_MAPS_API_KEY

from collections import namedtuple

LatLong = namedtuple("LatLong", "lat, long")


class Geolocation:
    def __init__(self):
        self.geolocator = GoogleV3(api_key=f"{GOOGLE_MAPS_API_KEY}", timeout=15)

    def get_lat_long_from_address(self, address: str) -> LatLong:
        try:
            location = self.geolocator.geocode(address)
        except Exception as error:
            # TODO: log the error:
            print(error)
            return LatLong(0, 0)

        if location:
            return LatLong(location.latitude, location.longitude)

        return LatLong(0, 0)
