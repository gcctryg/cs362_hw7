import unittest
import q2

class TestCase(unittest.TestCase):
    def test_leapYear(self):
        self.assertEqual(q2.leapYear(4), "This is a leap year!")

    def test_leapYear(self):
        self.assertEqual(q2.leapYear(200), "This is not a leap year!")


if __name__ == '__main__':
    unittest.main()