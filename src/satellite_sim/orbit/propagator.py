from datetime import datetime

from skyfield.api import EarthSatellite, load, wgs84

from satellite_sim.orbit.state import OrbitState

from satellite_sim.orbit.gp_data import GPData


class TLEOrbitPropagator:
    def __init__(self, tle_line_1: str, tle_line_2: str):
        self._timescale = load.timescale()

        self._satellite = EarthSatellite(
            tle_line_1,
            tle_line_2,
            ts=self._timescale,
        )

    def propagate(self, time: datetime) -> OrbitState:
        if time.tzinfo is None:
            raise ValueError("Propagation time must include a timezone")

        skyfield_time = self._timescale.from_datetime(time)

        geocentric = self._satellite.at(skyfield_time)

        geographic = wgs84.geographic_position_of(geocentric)

        return OrbitState(
            position_gcrs_km=tuple(float(x) for x in geocentric.xyz.km),
            velocity_gcrs_km_s=tuple(
                float(v) for v in geocentric.velocity.km_per_s
            ),
            latitude_deg=float(geographic.latitude.degrees),
            longitude_deg=float(geographic.longitude.degrees),
            altitude_km=float(geographic.elevation.km),
        )

class OMMOrbitPropagator:
    def __init__(self, gp_data: GPData):
        self._timescale = load.timescale()

        self._satellite = EarthSatellite.from_omm(
            self._timescale,
            gp_data.to_omm_fields(),
        )

    def propagate(self, time: datetime) -> OrbitState:
        if time.tzinfo is None:
            raise ValueError("Propagation time must include a timezone")

        skyfield_time = self._timescale.from_datetime(time)

        geocentric = self._satellite.at(skyfield_time)
        geographic = wgs84.geographic_position_of(geocentric)

        return OrbitState(
            position_gcrs_km=tuple(float(x) for x in geocentric.xyz.km),
            velocity_gcrs_km_s=tuple(
                float(v) for v in geocentric.velocity.km_per_s
            ),
            latitude_deg=float(geographic.latitude.degrees),
            longitude_deg=float(geographic.longitude.degrees),
            altitude_km=float(geographic.elevation.km),
        )