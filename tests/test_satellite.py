from satellite_sim.satellite import Satellite


def test_satellite_initial_state():
    satellite = Satellite("LEO-001")

    telemetry = satellite.get_telemetry()

    assert telemetry["name"] == "LEO-001"
    assert telemetry["battery_percent"] == 100.0