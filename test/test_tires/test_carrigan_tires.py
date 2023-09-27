import unittest

from tires.carrigan_tires import CarriganTire


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_data = [0.9, 0.4, 0.1, 0.2]

        tires = CarriganTire(tire_wear_data)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear_data = [0.2, 0.2, 0.1, 0.1]

        tires = CarriganTire(tire_wear_data)
        self.assertFalse(tires.needs_service())
