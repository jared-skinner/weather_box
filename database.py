from datetime import datetime
from random import randrange
import sqlite3

from weather_structs import Measurement
from interfaces import WeatherDB


class SqliteWeatherDB(WeatherDB):
    def __init__(self):
        # setup database, create variabels
        pass

    def store_measurement(self, measurement_date: datetime, measurement: Measurement) -> None:
        pass

    def get_measurement(self, measurement_date: datetime) -> Measurement:
        raise Exception()
        return Measurement(
            temperature=randrange(50, 80),
            accumulated_rain=randrange(0, 1)
        )
