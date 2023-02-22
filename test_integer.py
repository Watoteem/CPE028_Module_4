import unittest

class Integer(unittest.TestCase):
    def test_integer_different_value(x,y):
        x = 10
        y = 20
        assertIsNot(x,y)
    def test_integer_same_value(x,y):
        x = 10
        y = 10
        assertIs(x,y)

if __name__ == '__main__':
    
    unittest.main()