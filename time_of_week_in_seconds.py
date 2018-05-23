from datetime import datetime, timedelta

def current_time_to_sec(start, now):
    seconds_of_week = (now - start).total_seconds()
    return seconds_of_week

now = datetime.now()
timestart = (now - timedelta(days=now.weekday()+1)).replace(hour=0, minute=0, second=0, microsecond=0)
delta = current_time_to_sec(timestart, now)

print(delta)
