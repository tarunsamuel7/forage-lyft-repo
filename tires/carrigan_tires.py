from tires.tires import Tires


class CarriganTire(Tires):
    def __init__(self, tire_wear_data):
        self.tire_wear_data = tire_wear_data

    def needs_service(self):
        for tire in self.tire_wear_data:
            if tire >= 0.9:
                return True

        return False
