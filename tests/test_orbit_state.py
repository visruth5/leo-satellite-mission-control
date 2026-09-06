from satellite_sim.orbit.state import OrbitState


def test_orbit_state_stores_position_and_velocity():
    state = OrbitState(
        position_km=(1000.0, 2000.0, 3000.0),
        velocity_km_s=(1.0, 2.0, 3.0),
        latitude_deg=33.75,
        longitude_deg=-84.39,
        altitude_km=550.0,
    )

    assert state.position_km == (1000.0, 2000.0, 3000.0)
    assert state.velocity_km_s == (1.0, 2.0, 3.0)
    assert state.latitude_deg == 33.75
    assert state.longitude_deg == -84.39
    assert state.altitude_km == 550.0