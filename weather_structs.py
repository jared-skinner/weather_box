from datetime import datetime

from typing import NamedTuple

class Measurement(NamedTuple):
    temperature: float
    accumulated_rain: float

class Summary(NamedTuple):
    high: float
    low: float
    temp_window: tuple[datetime, datetime]

    accumulated_rain: float
    rain_window: tuple[datetime, datetime]
