from tires.tires import Tires


class OctoprimeTire(Tires):
    def __init__(self, tire_wear_data):
        self.tire_wear_data = tire_wear_data

    def needs_service(self):
        return sum(self.tire_wear_data) >= 3.0
