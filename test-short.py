import unittest 
import short

class Test(unittest.TestCase):

 #   def test_total_bill(self): #it checks the main method
  #      self.assertRaises(ValueError, short.process_input("",1,1,3))
    
    def test(self):
        self.assertRaises(ValueError, short.process_input(102,2))




if __name__ == '__main__':
    unittest.main()