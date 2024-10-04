from datetime import datetime
from abc import ABC, abstractmethod

from weather_structs import Measurement, Summary

class WeatherDB(ABC):
    @abstractmethod
    def store_measurement(self, measurement_date: datetime, measurement: Measurement) -> None:
        pass

    @abstractmethod
    def get_measurement(self, measurement_date: datetime) -> Measurement:
        pass

class WeatherDisplay(ABC):
    @abstractmethod
    def update(self, summary: Summary) -> None:
        pass

class WeatherAPI(ABC):
    @abstractmethod
    def get_measurement(self, measurement_date: datetime) -> Measurement:
        pass
