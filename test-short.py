import unittest 
import tipcalculatorclasses

class Test(unittest.TestCase):
    def test_totalbill(self): #it checks the main method
        self.assertRaises(TypeError, tipcalculatorclasses.process_input("f",2))
    
    def test_guests(self): #it checks the main method
        self.assertRaises(TypeError, tipcalculatorclasses.process_input(2.0,"h"))
   
    def test_isdividable1(self): #it checks the main method
        self.assertTrue(tipcalculatorclasses.process_input(102,2))
    
    def test_isdividable2(self): #it checks the main method
        self.assertFalse(tipcalculatorclasses.process_input(10,3))

if __name__ == '__main__':
    unittest.main()