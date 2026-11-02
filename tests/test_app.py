import unittest

from app import add_numbers, subtract_numbers


class TestApplication(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_subtraction(self):
        self.assertEqual(subtract_numbers(20, 10), 10)


if __name__ == "__main__":
    unittest.main()