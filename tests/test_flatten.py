import unittest
from src.flatten import flatten

class TestFlatten(unittest.TestCase):

    def test_simple_list(self):
        lista = [1, 2, 3, 4]
        esperada = [1, 2, 3, 4]
        self.assertEqual(flatten(lista), esperada)

    def test_nested_list(self):
        lista = [1, [2, 3], [4, [5, 6]]]
        esperada = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten(lista), esperada)

    def test_mixed_structures(self):
        lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
        esperada = [1, 2, 3, 'a', 4,'b' ,5 ,6 ,7 ,8]
        self.assertEqual(flatten(lista), esperada)

    def test_empty_list(self):
        self.assertEqual(flatten([]), [])

    def test_deeply_nested(self):
        lista = [1, [2, [3, [4, [5]]]]]
        esperada = [1, 2, 3, 4, 5]
        self.assertEqual(flatten(lista), esperada)

if __name__ == '__main__':
    unittest.main()