from datetime import datetime

from interfaces import Measurement, WeatherAPI, WeatherDB

class Collector:
    def __init__(self, apis: list[WeatherAPI], weather_db: WeatherDB):
        self.weather_db = weather_db
        self.apis = apis

    def get_measurement(self, measurement_date: datetime) -> Measurement:
        measurements: list[Measurement] = []
        for api in self.apis:
            measurement = api.get_measurement(measurement_date)
            measurements.append(measurement)

            # try to get measurement from db
            #try:
            #    # TODO: we want to check our cache, but if we can't find it there, we want to pull from the APIs
            #    measurmeent = self.weather_db.get_measurement(measurement_date)
            #except:
            #    measurement = api.get_measurement(measurement_date)
            #    self.weather_db.store_measurement(measurement_date, measurement)

        # for now just return the first api result
        return measurements[0]
