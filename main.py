from datetime import datetime, timedelta
from threading import Thread
from time import sleep

from collector import Collector
from database import SqliteWeatherDB
from display_basic import BasicWeatherDisplay
from display_eink import EinkWeatherDisplay
from interfaces import WeatherDisplay
from weather_apis import OWMWeatherAPI
from weather_window import WeatherWindow

def main_loop(window: WeatherWindow, display: WeatherDisplay):
    """
    Loop for automatic updates.  This may be removed later?
    """
    sleep_time: int = 1

    while True:
        display.update(window.get_summary())

        window.update(
            start_date=datetime.now() - timedelta(hours=100),
            end_date=datetime.now()
        )

        sleep(sleep_time)

def main():
    # TODO: this logic will need to live in a seperate thread so the ui can still be responsive
    db = SqliteWeatherDB()
    weather_collector = Collector(apis=[OWMWeatherAPI()], weather_db=db)

    window = WeatherWindow(
        start_date=datetime.now() - timedelta(hours=100),
        end_date=datetime.now(),
        weather_collector=weather_collector
    )

    eink_display = EinkWeatherDisplay()
    basic_display = BasicWeatherDisplay()

    #t1 = Thread(target=main_loop, args=(window, basic_display))
    #t1.start()

    sleep_time: int = 30

    while True:
        basic_display.update(window.get_summary())

        window.update(
            start_date=datetime.now() - timedelta(hours=100),
            end_date=datetime.now()
        )

        sleep(sleep_time)


    while True:
        sleep(1000)

if __name__ == "__main__":
    main()
