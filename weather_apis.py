from pyowm import OWM
from secrets import OMW_API_KEY
import requests
from datetime import datetime

from weather_structs import Measurement
from interfaces import WeatherAPI

class OWMWeatherAPI(WeatherAPI):
    """ 
    Open Weather Map API
    """
    def __init__(self):
        self.latitude=45.0419073
        self.longitude=-93.7891331
        self.OWMUrl = f"https://api.openweathermap.org/data/3.0/onecall?lat={self.latitude}&lon={self.longitude}&exclude=minutely,daily&units=imperial&appid={OMW_API_KEY}"
        self.one_call_results = self.call_api()

    def call_api(self) -> str:
        response = requests.get(self.OWMUrl)
        if response.status_code == 200:
            wedata = response.json()
            return wedata
        else:
            return ""

    def get_measurement(self, measurement_date: datetime) -> Measurement:
        return Measurement(temperature=self.one_call_results["current"]["temp"], accumulated_rain=0.0)


"""
{
    'dt'        : 1727997352,
    'sunrise'   : 1727957769,
    'sunset'    : 1727999498,
    'temp'      : 55.2,
    'feels_like': 52.95,
    'pressure'  : 1021,
    'humidity'  : 54,
    'dew_point' : 38.88,
    'uvi'       : 0.15,
    'clouds'    : 40,
    'visibility': 10000,
    'wind_speed': 8.05,
    'wind_deg'  : 350,
    'weather'   : [
        {
            'id': 802,
            'main': 'Clouds',
            'description': 'scattered clouds',
            'icon': '03d'
        }
    ]
}
"""
