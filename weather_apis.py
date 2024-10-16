from pyowm import OWM
from secrets import OMW_API_KEY
import requests
from datetime import datetime
import json

from weather_structs import Measurement
from interfaces import WeatherAPI
from hardcoded_api_response import HARD_CODED_RESPONSE

class OWMWeatherAPI(WeatherAPI):
    def __init__(self):
        self.latitude=45.0419073
        self.longitude=-93.7891331
        self.OWMUrl = f"https://api.openweathermap.org/data/3.0/onecall?lat={self.latitude}&lon={self.longitude}&exclude=minutely,daily&units=imperial&appid={OMW_API_KEY}"
        self.one_call_results = self.call_api()
        self.measurements: dict[int, Measurement] = self.compile_measurements()

    def call_api(self) -> str:
        #return json.loads(HARD_CODED_RESPONSE)
        response = requests.get(self.OWMUrl)

        wedata = response.json()

        if response.status_code == 200:
            wedata = response.json()
            return wedata
        else:
            # TODO: catch other response codes!
            return ""

    def build_measurement_from_json(self, measurement_json) -> Measurement:
        return Measurement(
            temperature = measurement_json["temp"],
            accumulated_rain = 0
        )

    def compile_measurements(self) -> dict[int, Measurement]:
        measurement_json = self.call_api()
        measurements: dict[int, Measurement] = {}
        measurements[measurement_json["current"]["dt"]] = self.build_measurement_from_json(measurement_json["current"])
        for hourly_json in measurement_json["hourly"]:
            measurements[hourly_json["dt"]] = self.build_measurement_from_json(hourly_json)

        return measurements

    def get_measurement(self, measurement_date: datetime) -> Measurement:
        # convert the datetime into a timestamp
        timestamp = int(datetime.timestamp(measurement_date))
        print(timestamp)
        try:
            return self.measurements[timestamp]
        except:
            # TODO: handle this gracefully
            return Measurement(temperature=self.one_call_results["current"]["temp"], accumulated_rain=0.0)
