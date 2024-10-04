from datetime import datetime

from interfaces import Measurement, WeatherAPI

class Collector:
    def __init__(self, apis: list[WeatherAPI]):
        self.apis = apis

    def get_measurement(self, measurement_date: datetime) -> Measurement:
        measurements: list[Measurement] = []
        for api in self.apis:
            measurements.append(api.get_measurement(measurement_date))

        return measurements[0]
