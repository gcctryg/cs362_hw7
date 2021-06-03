import unittest
import q1

class TestCaseAdd(unittest.TestCase):
    def test_3(self):
        for i in [3, 6, 9, 12]:
            self.assertEqual(q1.fizzbuzz(i), "Fizz")

    def test_5(self):
        for i in [5, 10, 20, 25]:
            self.assertEqual(q1.fizzbuzz(i), "Buzz")

    def test_3and5(self):
        for i in [15, 45, 75]:
            self.assertEqual(q1.fizzbuzz(i), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()