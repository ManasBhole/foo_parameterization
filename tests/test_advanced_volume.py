import unittest
from foo.advanced_volume import calculate_advanced_volume

class TestAdvancedVolumeCalculation(unittest.TestCase):
    def test_advanced_calculation(self):
        self.assertAlmostEqual(calculate_advanced_volume(1, 1.0, 300), 4.1887902047863905)

if __name__ == "__main__":
    unittest.main()