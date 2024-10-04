from weather_structs import Summary
from interfaces import WeatherDisplay

class BasicWeatherDisplay(WeatherDisplay):
    def update(self, summary: Summary) -> None:
        """ 
        update the display
        """
        print(f"Temp Window:      {summary.temp_window[0]} to {summary.temp_window[1]}")
        print(f"High:             {summary.high}")
        print(f"Low:              {summary.low}")
        print("")
        print(f"Rain Window:      {summary.rain_window[0]} to {summary.rain_window[1]}")
        print(f"Accumulated Rain: {summary.accumulated_rain}")
        print("")
        print("")

