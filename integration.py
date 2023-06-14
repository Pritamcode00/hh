import unittest
from sum import sum
from subtract import subtract
from multiply import multiply
from divide import divide

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        result = sum(1, 2)
        result = subtract(result, 1)
        result = multiply(result, 3)
        result = divide(result, 2)
        self.assertEqual(result, 1.5)

if __name__ == '__main__':
    unittest.main()

