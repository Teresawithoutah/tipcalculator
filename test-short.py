import unittest 
import tipcalculatorclasses

class Test(unittest.TestCase):

 #   def test_total_bill(self): #it checks the main method
  #      self.assertRaises(ValueError, short.process_input("",1,1,3))
    
    def test_dividable1(self):
        self.assertTrue(tipcalculatorclasses.process_input(102,2))
    def test_dividable2(self):
        self.assertTrue(tipcalculatorclasses.process_input(10,3))




if __name__ == '__main__':
    unittest.main()