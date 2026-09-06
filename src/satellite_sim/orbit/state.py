from dataclasses import dataclass


@dataclass
class OrbitState:
    position_km: tuple[float, float, float]
    velocity_km_s: tuple[float, float, float]
    latitude_deg: float
    longitude_deg: float
    altitude_km: float