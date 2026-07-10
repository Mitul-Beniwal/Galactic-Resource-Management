# src/utils.py

from datetime import datetime

def log_mission(func):
    def wrapper(self, *args, **kwargs):
        start = datetime.now()
        print(f"Time at which the mission started is: ({start})")
        return func(self, *args, **kwargs)
    return wrapper

class LowFuelError(Exception):
    pass