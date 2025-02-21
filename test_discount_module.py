# test_discount_module.py
import unittest
from disount_module import apply_discount

class TestDiscountModule(unittest.TestCase):

    def test_no_discount(self):
        self.assertEqual(apply_discount(500), 500)
        self.assertEqual(apply_discount(100), 100)
    
    def test_five_percent_discount(self):
        self.assertEqual(apply_discount(600), 570)  
        self.assertEqual(apply_discount(800), 760)

    def test_ten_percent_discount(self):
        self.assertEqual(apply_discount(1200), 1080)
        self.assertEqual(apply_discount(1500), 1350)  

if __name__ == '__main__':
    unittest.main()
