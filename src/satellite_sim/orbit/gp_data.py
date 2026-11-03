from dataclasses import dataclass


@dataclass
class GPData:
    object_name: str
    object_id: str
    epoch: str

    mean_motion: float
    eccentricity: float
    inclination_deg: float
    ra_of_asc_node_deg: float
    arg_of_pericenter_deg: float
    mean_anomaly_deg: float

    ephemeris_type: int
    classification_type: str
    norad_cat_id: int
    element_set_no: int
    rev_at_epoch: int

    bstar: float
    mean_motion_dot: float
    mean_motion_ddot: float

    def to_omm_fields(self) -> dict[str, str | int | float]:
        return {
            "OBJECT_NAME": self.object_name,
            "OBJECT_ID": self.object_id,
            "EPOCH": self.epoch,
            "MEAN_MOTION": self.mean_motion,
            "ECCENTRICITY": self.eccentricity,
            "INCLINATION": self.inclination_deg,
            "RA_OF_ASC_NODE": self.ra_of_asc_node_deg,
            "ARG_OF_PERICENTER": self.arg_of_pericenter_deg,
            "MEAN_ANOMALY": self.mean_anomaly_deg,
            "EPHEMERIS_TYPE": self.ephemeris_type,
            "CLASSIFICATION_TYPE": self.classification_type,
            "NORAD_CAT_ID": self.norad_cat_id,
            "ELEMENT_SET_NO": self.element_set_no,
            "REV_AT_EPOCH": self.rev_at_epoch,
            "BSTAR": self.bstar,
            "MEAN_MOTION_DOT": self.mean_motion_dot,
            "MEAN_MOTION_DDOT": self.mean_motion_ddot,
        }