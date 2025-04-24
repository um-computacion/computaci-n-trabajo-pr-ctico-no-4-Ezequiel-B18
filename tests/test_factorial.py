import unittest
from src.factorial import factorial_iterative, factorial_recursive

class TestFactorial(unittest.TestCase):

    #Tests iterativos

    def test_factorial_iterative_zero(self):
        self.assertEqual(factorial_iterative(0), 1)

    def test_factorial_iterative_small(self):
        self.assertEqual(factorial_iterative(2), 2)
        self.assertEqual(factorial_iterative(3), 6)
        self.assertEqual(factorial_iterative(4), 24)

    def test_factorial_iterative_medium(self):
        self.assertEqual(factorial_iterative(8), 40320)
        
    def test_factorial_iterative_negative(self):
        with self.assertRaises(ValueError):
            factorial_iterative(-1)

    #Tests recursivos

    def test_factorial_recursive_zero(self):
        self.assertEqual(factorial_iterative(0), 1)

    def test_factorial_recursive_small(self):
        self.assertEqual(factorial_recursive(2), 2)
        self.assertEqual(factorial_recursive(3), 6)
        self.assertEqual(factorial_recursive(4), 24)

    def test_factorial_recursive_medium(self):
        self.assertEqual(factorial_recursive(8), 40320)
        
    def test_factorial_recursive_negative(self):
        with self.assertRaises(ValueError):
            factorial_recursive(-1)

if __name__ == '__main__':
    unittest.main()