import unittest
from foo.volume import calculate_volume

class TestVolumeCalculation(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(calculate_volume(1), 4.1887902047863905)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1)

if __name__ == "__main__":
    unittest.main()