class Satellite:
    def __init__(self, name: str):
        self.name = name
        self.altitude_km = 550.0
        self.battery_percent = 100.0
        self.temperature_c = 20.0

    def get_telemetry(self):
        return {
            "name": self.name,
            "altitude_km": self.altitude_km,
            "battery_percent": self.battery_percent,
            "temperature_c": self.temperature_c,
        }