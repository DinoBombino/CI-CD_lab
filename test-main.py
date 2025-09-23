import unittest
from main import add

class TestAdd(unittest.TestCase):
    def test_add_pos(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_add_pos2(self):
        self.assertEqual(add(3, 3), 6)

    def test_add_neg(self):
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()