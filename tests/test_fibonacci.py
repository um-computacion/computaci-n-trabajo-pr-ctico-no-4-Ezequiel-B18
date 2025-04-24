import unittest
from src.fibonacci import fibonacci_iterative, fibonacci_recursive

class TestFibonacci(unittest.TestCase):

    #Tests para la funcion iterativa

    def test_fibonacci_iterative_base(self):
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(1), 1)

    def test_fibonacci_iterative_small(self):
        self.assertEqual(fibonacci_iterative(2), 1)
        self.assertEqual(fibonacci_iterative(3), 2)
        self.assertEqual(fibonacci_iterative(4), 3)
        self.assertEqual(fibonacci_iterative(5), 5)

    def test_fibonacci_iterative_medium(self):
        self.assertEqual(fibonacci_iterative(8), 21)
        self.assertEqual(fibonacci_iterative(10), 55)

    def test_fibonacci_iterative_negative(self):
        with self.assertRaises(ValueError):
            fibonacci_iterative(-1)
        
    #Tests para la funcion recursiva

    # def test_fibonacci_recursive_base(self):
    #     self.assertEqual(fibonacci_recursive(0), 0)
    #     self.assertEqual(fibonacci_recursive(1), 1)

    # def test_fibonacci_recursive_small(self):
    #     self.assertEqual(fibonacci_recursive(2), 1)
    #     self.assertEqual(fibonacci_recursive(3), 2)
    #     self.assertEqual(fibonacci_recursive(4), 3)
    #     self.assertEqual(fibonacci_recursive(5), 5)

    # def test_fibonacci_recursive_medium(self):
    #     self.assertEqual(fibonacci_recursive(8), 21)
    #     self.assertEqual(fibonacci_recursive(10), 55)

    # def test_fibonacci_recursive_negative(self):
    #     with self.assertRaises(ValueError):
    #         fibonacci_recursive(-1)

if __name__ == '__main__':
    unittest.main()