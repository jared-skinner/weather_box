from collector import Collector
from datetime import datetime, timedelta
from weather_structs import Measurement, Summary
from utils import round_datetime_to_nearest_hour

class WeatherWindow:
    def __init__(self, start_date: datetime, end_date: datetime, weather_collector: Collector) -> None:
        self.start_date: datetime = round_datetime_to_nearest_hour(start_date)
        self.end_date: datetime = round_datetime_to_nearest_hour(end_date)
        self.high: float
        self.low: float
        self.weather_collector = weather_collector

        self.measurement_window: dict[datetime, Measurement] = self.load_window()
        self.high, self.low = self.get_high_and_low()
        self.accumulated_rain: float = self.get_accumulated_rain()

    def update(self, start_date: datetime, end_date: datetime) -> None:
        self.start_date = round_datetime_to_nearest_hour(start_date)
        self.end_date = round_datetime_to_nearest_hour(end_date)

        self.measurement_window: dict[datetime, Measurement] = self.load_window()
        self.high, self.low = self.get_high_and_low()
        self.accumulated_rain: float = self.get_accumulated_rain()

    def get_high_and_low(self) -> tuple[float, float]:
        high: float = self.measurement_window[self.start_date].temperature
        low: float = self.measurement_window[self.start_date].temperature

        for _, measurement in self.measurement_window.items():
            if high < measurement.temperature:
                high = measurement.temperature

            if low > measurement.temperature:
                low = measurement.temperature

        return high, low

    def get_accumulated_rain(self, hours_back: int = 6) -> float:
        i = 1
        accumulated_rain: float = 0
        while i < hours_back:
            i += 1
            accumulated_rain += self.measurement_window[self.end_date - timedelta(hours=i)].accumulated_rain

        return accumulated_rain

    def load_window(self) -> dict[datetime, Measurement]:
        window: dict[datetime, Measurement] = {}
        measurement_date: datetime = self.start_date
        while measurement_date <= self.end_date:
            window[measurement_date] = self.weather_collector.get_measurement(measurement_date)
            measurement_date = measurement_date + timedelta(hours=1)

        return window

    def get_summary(self) -> Summary:
        return Summary(
            high = self.high,
            low = self.low,
            accumulated_rain = self.accumulated_rain,
            temp_window = (self.start_date, self.end_date),
            rain_window = (self.start_date, self.end_date) # TODO, this should be a different window
        )
