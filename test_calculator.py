import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(-3, -6), 3)
        self.assertEqual(sub(5, 10), -5)


    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(2, -2), -4)
        self.assertEqual(mul(-2, -2), 4)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 2), 1)
        self.assertEqual(div(2, -2), -1)
        self.assertEqual(div(-2, -2), 1)
    ##########################


    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 1000), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(0, 10)
        with self.assertRaises(ValueError):
            log(-2, 8)
        with self.assertRaises(ValueError):
            log(2, -5)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError): log(0, 5)
        

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-1)
    #     # Test basic function
        self.assertEqual(square_root(4), 2)
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()