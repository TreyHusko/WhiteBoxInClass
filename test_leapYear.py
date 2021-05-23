import unittest
import leapYear

class testCaseLeapYear(unittest.TestCase):
    def test_LeapYear(self):
        # result =  leapYear.isLeapYear(2000)
        self.assertEqual(leapYear.isLeapYear(2000), True)
    def test_LeapYear2(self):
        # result =  leapYear.isLeapYear(1700)
        self.assertEqual(leapYear.isLeapYear(1700), False)
    def test_LeapYear3(self):
        # result =  leapYear.isLeapYear(1900)
        self.assertEqual(leapYear.isLeapYear(1900), True)
    def test_LeapYear4(self):
        # result =  leapYear.isLeapYear(1600)
        self.assertEqual(leapYear.isLeapYear(1600), False)
    def test_LeapYear6(self):
        # result =  leapYear.isLeapYear(2020)
        self.assertEqual(leapYear.isLeapYear(2020), True)


if __name__ == "__main__":
    unittest.main()