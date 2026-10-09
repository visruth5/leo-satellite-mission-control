from datetime import datetime, timezone

import pytest

from satellite_sim.orbit.propagator import TLEOrbitPropagator
from satellite_sim.orbit.state import OrbitState


TLE_LINE_1 = (
    "1 25544U 98067A   24127.82853009  .00015698  00000+0  27310-3 0  9995"
)

TLE_LINE_2 = (
    "2 25544  51.6393 160.4574 0003580 140.6673 205.7250 15.50957674452123"
)

def test_propagate_rejects_naive_datetime():
    propagator = TLEOrbitPropagator(TLE_LINE_1, TLE_LINE_2)

    time = datetime(2024, 5, 6, 20, 0, 0)

    with pytest.raises(ValueError):
        propagator.propagate(time)

def test_propagate_returns_reasonable_leo_state():
    propagator = TLEOrbitPropagator(TLE_LINE_1, TLE_LINE_2)

    time = datetime(
        2024,
        5,
        6,
        20,
        0,
        0,
        tzinfo=timezone.utc,
    )

    state = propagator.propagate(time)

    assert isinstance(state, OrbitState)

    assert 300.0 < state.altitude_km < 500.0
    assert 7.0 < sum(v**2 for v in state.velocity_gcrs_km_s) ** 0.5 < 8.5

    assert -90.0 <= state.latitude_deg <= 90.0
    assert -180.0 <= state.longitude_deg <= 180.0