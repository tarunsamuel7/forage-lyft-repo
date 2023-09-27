import unittest

from tires.octoprime_tires import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_data = [0.9, 0.8, 0.8, 0.7]

        tires = OctoprimeTire(tire_wear_data)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear_data = [0.2, 0.2, 0.1, 0.1]

        tires = OctoprimeTire(tire_wear_data)
        self.assertFalse(tires.needs_service())
