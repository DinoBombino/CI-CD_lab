import unittest
from main import add, min

class TestAdd(unittest.TestCase):
    def test_add_pos(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_add_pos2(self):
        self.assertEqual(add(3, 3), 6)
        
    def test_add_pos3(self):
        self.assertEqual(add(3, 4), 7)

    def test_add_neg(self):
        self.assertEqual(add(-1, 1), 0)

class TestMin(unittest.TestCase):
    def test_min(self):
        self.assertEqual(min(8, 3), 5)

if __name__ == '__main__':
    unittest.main()