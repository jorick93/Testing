"""
GPS location helper.

Author: Jorick van Brunschot
Created: 2026-06-10
Version: 1.0.0

Description:
    Helper functions for calculating GPS locations and distances.

Features:
    - Convert compass directions to degrees.
    - Calculate a new latitude/longitude from a start point, distance, and direction.
    - Calculate the distance in meters between two GPS locations.

Notes:
    - Coordinates use decimal degrees.
    - Distance is calculated in meters.
    - Direction can be a compass direction, such as "N", "NE", "SW",
      or a degree value, such as "90" or "225".
"""

import math

DIRECTION_TO_DEGREES = {
    "N": 0,
    "NORTH": 0,
    "NNE": 22.5,
    "NE": 45,
    "NORTHEAST": 45,
    "ENE": 67.5,
    "E": 90,
    "EAST": 90,
    "ESE": 112.5,
    "SE": 135,
    "SOUTHEAST": 135,
    "SSE": 157.5,
    "S": 180,
    "SOUTH": 180,
    "SSW": 202.5,
    "SW": 225,
    "SOUTHWEST": 225,
    "WSW": 247.5,
    "W": 270,
    "WEST": 270,
    "WNW": 292.5,
    "NW": 315,
    "NORTHWEST": 315,
    "NNW": 337.5,
}

def parse_direction(direction: str) -> float:
    """
    Convert a compass direction or degree value to degrees.

    Examples:
    - "N" -> 0
    - "E" -> 90
    - "SW" -> 225
    - "450" -> 90

    Args:
        direction: Compass direction or degree value as text.

    Returns:
        Direction in degrees between 0 and 360.

    Raises:
        ValueError: If the direction is invalid.
    """

    direction = direction.strip().upper()

    if direction in DIRECTION_TO_DEGREES:
        return DIRECTION_TO_DEGREES[direction]

    try:
        return float(direction) % 360
    except ValueError as exc:
        raise ValueError(f"Invalid direction: {direction}") from exc

def calculate_new_location(
    latitude: float,
    longitude: float,
    distance_meters: float,
    direction: str,
) -> tuple[float, float]:
    """
    Calculate a new GPS location from a start point, distance, and direction.

    Args:
        latitude: Start latitude in decimal degrees.
        longitude: Start longitude in decimal degrees.
        distance_meters: Distance to move in meters.
        direction: Compass direction or degrees, for example "N", "SW" or "90".

    Returns:
        New latitude and longitude as a tuple.
    """

    earth_radius_meters = 6_371_000

    bearing_degrees = parse_direction(direction)
    bearing_radians = math.radians(bearing_degrees)

    lat1 = math.radians(latitude)
    lon1 = math.radians(longitude)

    angular_distance = distance_meters / earth_radius_meters

    lat2 = math.asin(
        math.sin(lat1) * math.cos(angular_distance)
        + math.cos(lat1) * math.sin(angular_distance) * math.cos(bearing_radians)
    )

    lon2 = lon1 + math.atan2(
        math.sin(bearing_radians) * math.sin(angular_distance) * math.cos(lat1),
        math.cos(angular_distance) - math.sin(lat1) * math.sin(lat2),
    )

    new_latitude = math.degrees(lat2)
    new_longitude = math.degrees(lon2)

    new_longitude = (new_longitude + 540) % 360 - 180

    return new_latitude, new_longitude

def calculate_distance_meters(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
) -> float:
    """
    Calculate the distance in meters between two GPS locations.

    Args:
        lat1: Latitude of the first location.
        lon1: Longitude of the first location.
        lat2: Latitude of the second location.
        lon2: Longitude of the second location.

    Returns:
        Distance in meters.
    """

    earth_radius_meters = 6_371_000

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1_rad)
        * math.cos(lat2_rad)
        * math.sin(delta_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius_meters * c

def calculate_3d_distance_meters(
    lat1: float,
    lon1: float,
    alt1: float,
    lat2: float,
    lon2: float,
    alt2: float,
) -> float:
    """
    Calculate the 3D distance in meters between two GPS locations.

    Args:
        lat1: Latitude of the first location.
        lon1: Longitude of the first location.
        alt1: Altitude of the first location in meters.
        lat2: Latitude of the second location.
        lon2: Longitude of the second location.
        alt2: Altitude of the second location in meters.

    Returns:
        3D distance in meters, including altitude difference.
    """

    horizontal_distance = calculate_distance_meters(
        lat1=lat1,
        lon1=lon1,
        lat2=lat2,
        lon2=lon2,
    )

    altitude_difference = alt2 - alt1

    return math.sqrt(horizontal_distance**2 + altitude_difference**2)

if __name__ == "__main__":


    # Distance tests
    assert calculate_distance_meters(
        52.3676,
        4.9041,
        52.3676,
        4.9041,
    ) == 0


    # Shift 100 meters north
    start_lat = 52.3676
    start_lon = 4.9041

    new_lat, new_lon = calculate_new_location(
        latitude=start_lat,
        longitude=start_lon,
        distance_meters=100,
        direction="N",
    )

    distance = calculate_distance_meters(
        start_lat,
        start_lon,
        new_lat,
        new_lon,
    )

    assert round(distance, 1) == 100.0
    assert new_lat > start_lat
    assert round(new_lon, 5) == round(start_lon, 5)


    # Shift 100 meters east
    new_lat, new_lon = calculate_new_location(
        latitude=start_lat,
        longitude=start_lon,
        distance_meters=100,
        direction="E",
    )

    distance = calculate_distance_meters(
        start_lat,
        start_lon,
        new_lat,
        new_lon,
    )

    assert round(distance, 1) == 100.0
    assert new_lon > start_lon
    assert round(new_lat, 5) == round(start_lat, 5)


    # Shift 250 meters southwest
    new_lat, new_lon = calculate_new_location(
        latitude=start_lat,
        longitude=start_lon,
        distance_meters=250,
        direction="SW",
    )

    distance = calculate_distance_meters(
        start_lat,
        start_lon,
        new_lat,
        new_lon,
    )

    assert round(distance, 1) == 250.0
    assert new_lat < start_lat
    assert new_lon < start_lon
    
    # Same location and same altitude
    assert calculate_3d_distance_meters(
        52.3676,
        4.9041,
        10,
        52.3676,
        4.9041,
        10,
    ) == 0


    # Same location, 10 meters altitude difference
    assert calculate_3d_distance_meters(
        52.3676,
        4.9041,
        10,
        52.3676,
        4.9041,
        20,
    ) == 10


    # 100 meters north and 0 meters altitude difference
    start_lat = 52.3676
    start_lon = 4.9041

    new_lat, new_lon = calculate_new_location(
        latitude=start_lat,
        longitude=start_lon,
        distance_meters=100,
        direction="N",
    )

    distance_3d = calculate_3d_distance_meters(
        start_lat,
        start_lon,
        10,
        new_lat,
        new_lon,
        10,
    )

    assert round(distance_3d, 1) == 100.0


    print("All location helper tests passed.")
