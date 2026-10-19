from datetime import datetime, timezone

from satellite_sim.orbit.gp_data import GPData
from satellite_sim.orbit.propagator import OMMOrbitPropagator
from satellite_sim.orbit.state import OrbitState


def test_omm_propagator_returns_reasonable_leo_state():
    data = GPData(
        object_name="ISS (ZARYA)",
        object_id="1998-067A",
        epoch="2024-05-06T19:53:04.999776",
        mean_motion=15.50957674,
        eccentricity=0.000358,
        inclination_deg=51.6393,
        ra_of_asc_node_deg=160.4574,
        arg_of_pericenter_deg=140.6673,
        mean_anomaly_deg=205.7250,
        ephemeris_type=0,
        classification_type="U",
        norad_cat_id=25544,
        element_set_no=999,
        rev_at_epoch=45212,
        bstar=0.0002731,
        mean_motion_dot=0.00015698,
        mean_motion_ddot=0.0,
    )

    propagator = OMMOrbitPropagator(data)

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
    assert (
        7.0
        < sum(v**2 for v in state.velocity_gcrs_km_s) ** 0.5
        < 8.5
    )
    assert -90.0 <= state.latitude_deg <= 90.0
    assert -180.0 <= state.longitude_deg <= 180.0