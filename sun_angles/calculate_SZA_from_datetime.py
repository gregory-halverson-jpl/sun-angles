from datetime import datetime
from rasters import CoordinateArray
from .SZA_deg_from_lat_dec_hour import SZA_deg_from_lat_dec_hour
from .calculate_SZA_from_DOY_and_hour import calculate_SZA_from_DOY_and_hour
from solar_apparent_time import solar_day_of_year_for_longitude, solar_hour_of_day_for_area

def calculate_SZA_from_datetime(time_UTC: datetime, lat: float, lon: float):
    """
    Calculates the solar zenith angle (SZA) in degrees based on the given UTC time, latitude, and longitude.

    Args:
        time_UTC (datetime.datetime): The UTC time to calculate the SZA for.
        lat (float): The latitude in degrees.
        lon (float): The longitude in degrees.

    Returns:
        float: The calculated solar zenith angle in degrees.
    """
    # Calculate the day of year based on the UTC time and longitude
    doy = solar_day_of_year_for_longitude(time_UTC, lon)
    # Calculate the hour of the day based on the UTC time and longitude
    hour = solar_hour_of_day_for_area(time_UTC=time_UTC, geometry=CoordinateArray(x=lon, y=lat))
    # Calculate the solar zenith angle in degrees based on the latitude, solar declination angle, and hour of the day
    SZA = calculate_SZA_from_DOY_and_hour(lat, lon, doy, hour)

    # Return the calculated solar zenith angle
    return SZA
