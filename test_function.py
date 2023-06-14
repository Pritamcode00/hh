import unittest
from sum import sum
from subtract import subtract
from multiply import multiply
from divide import divide

class TestFunctions(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(3, 1), 2)
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(-4, 2), -2)
        self.assertEqual(divide(-4, -2), 2)
        with self.assertRaises(ValueError):
            divide(4, 0)

if __name__ == '__main__':
    unittest.main()

