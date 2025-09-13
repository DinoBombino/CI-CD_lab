import unittest
from main import add, subtract

class TestAdd(unittest.TestCase):
    def test_add_pos(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_neg(self):
        self.assertEqual(add(-1, 1), 0)

class TestSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()