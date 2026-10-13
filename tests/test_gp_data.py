from satellite_sim.orbit.gp_data import GPData


def test_gp_data_stores_orbital_elements():
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

    assert data.object_name == "ISS (ZARYA)"
    assert data.norad_cat_id == 25544
    assert data.inclination_deg == 51.6393
    assert data.bstar == 0.0002731

def test_gp_data_converts_to_omm_fields():
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

    fields = data.to_omm_fields()

    assert fields["OBJECT_NAME"] == "ISS (ZARYA)"
    assert fields["NORAD_CAT_ID"] == 25544
    assert fields["INCLINATION"] == 51.6393
    assert fields["BSTAR"] == 0.0002731
