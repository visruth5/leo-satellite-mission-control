import httpx
import pytest

from satellite_sim.orbit.celestrak_client import CelesTrakGPClient
from satellite_sim.orbit.gp_data import GPData


class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return [
            {
                "OBJECT_NAME": "ISS (ZARYA)",
                "OBJECT_ID": "1998-067A",
                "EPOCH": "2024-05-06T19:53:04.999776",
                "MEAN_MOTION": "15.50957674",
                "ECCENTRICITY": "0.0003580",
                "INCLINATION": "51.6393",
                "RA_OF_ASC_NODE": "160.4574",
                "ARG_OF_PERICENTER": "140.6673",
                "MEAN_ANOMALY": "205.7250",
                "EPHEMERIS_TYPE": "0",
                "CLASSIFICATION_TYPE": "U",
                "NORAD_CAT_ID": "25544",
                "ELEMENT_SET_NO": "999",
                "REV_AT_EPOCH": "45212",
                "BSTAR": "0.00027310",
                "MEAN_MOTION_DOT": "0.00015698",
                "MEAN_MOTION_DDOT": "0.0",
            }
        ]


def test_fetch_by_catalog_id_returns_gp_data(monkeypatch):
    def fake_get(url, params, timeout):
        assert url == CelesTrakGPClient.BASE_URL
        assert params == {
            "CATNR": 25544,
            "FORMAT": "JSON",
        }
        assert timeout == 10.0

        return FakeResponse()

    monkeypatch.setattr(httpx, "get", fake_get)

    client = CelesTrakGPClient()
    data = client.fetch_by_catalog_id(25544)

    assert isinstance(data, GPData)
    assert data.object_name == "ISS (ZARYA)"
    assert data.norad_cat_id == 25544
    assert data.inclination_deg == 51.6393

def test_fetch_by_catalog_id_raises_when_satellite_not_found(monkeypatch):
    class EmptyResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return []

    def fake_get(url, params, timeout):
        return EmptyResponse()

    monkeypatch.setattr(httpx, "get", fake_get)

    client = CelesTrakGPClient()

    with pytest.raises(ValueError, match="No satellite found"):
        client.fetch_by_catalog_id(999999999)

def test_fetch_by_catalog_id_raises_for_malformed_record(monkeypatch):
    class MalformedResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return [
                {
                    "OBJECT_NAME": "ISS (ZARYA)"
                }
            ]

    def fake_get(url, params, timeout):
        return MalformedResponse()

    monkeypatch.setattr(httpx, "get", fake_get)

    client = CelesTrakGPClient()

    with pytest.raises(ValueError, match="Malformed CelesTrak response"):
        client.fetch_by_catalog_id(25544)