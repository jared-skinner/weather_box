from datetime import datetime, timedelta

def round_datetime_to_nearest_hour(t: datetime) -> datetime:
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
               +timedelta(hours=t.minute//30))
