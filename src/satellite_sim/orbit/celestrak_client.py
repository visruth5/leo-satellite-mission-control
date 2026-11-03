import httpx

from satellite_sim.orbit.gp_data import GPData


class CelesTrakGPClient:
    BASE_URL = "https://celestrak.org/NORAD/elements/gp.php"

    def fetch_by_catalog_id(self, catalog_id: int) -> GPData:
        response = httpx.get(
            self.BASE_URL,
            params={
                "CATNR": catalog_id,
                "FORMAT": "JSON",
            },
            timeout=10.0,
        )

        response.raise_for_status()

        records = response.json()

        if not records:
            raise ValueError(f"No satellite found for catalog ID {catalog_id}")

        record = records[0]
        
        try:
            return GPData(
                object_name=record["OBJECT_NAME"],
                object_id=record["OBJECT_ID"],
                epoch=record["EPOCH"],
                mean_motion=float(record["MEAN_MOTION"]),
                eccentricity=float(record["ECCENTRICITY"]),
                inclination_deg=float(record["INCLINATION"]),
                ra_of_asc_node_deg=float(record["RA_OF_ASC_NODE"]),
                arg_of_pericenter_deg=float(record["ARG_OF_PERICENTER"]),
                mean_anomaly_deg=float(record["MEAN_ANOMALY"]),
                ephemeris_type=int(record["EPHEMERIS_TYPE"]),
                classification_type=record["CLASSIFICATION_TYPE"],
                norad_cat_id=int(record["NORAD_CAT_ID"]),
                element_set_no=int(record["ELEMENT_SET_NO"]),
                rev_at_epoch=int(record["REV_AT_EPOCH"]),
                bstar=float(record["BSTAR"]),
                mean_motion_dot=float(record["MEAN_MOTION_DOT"]),
                mean_motion_ddot=float(record["MEAN_MOTION_DDOT"]),
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError("Malformed CelesTrak response") from exc
