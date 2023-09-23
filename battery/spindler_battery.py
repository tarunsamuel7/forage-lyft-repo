from battery.battery import Battery
import pandas as pd


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        next_service_date = pd.to_datetime(self.last_service_date) + pd.DateOffset(
            years=2
        )

        if next_service_date < self.current_date:
            return False

        return True
