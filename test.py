import unittest
import subprocess

from main import parse_input
from itinerary_generator.helper import itinerary_from_number, check_can_satisfy

class TestMain(unittest.TestCase):

    def test_parse_input(self):

        # Test case 1
        lines = ["0 airborne, 3 by-sea, 5 by-sea", "1 airborne, 4 by-sea", "0 by-sea, 2 airborne"]
        result = parse_input(lines)
        expected_result = [{0: "airborne", 3: "by-sea", 5: "by-sea"},
                        {1: "airborne", 4: "by-sea"},
                        {0: "by-sea", 2: "airborne"}]
        self.assertEqual(result, expected_result)

        # Test case 2
        lines = ["2 airborne, 4 by-sea", "3 airborne", "0 by-sea, 2 airborne, 4 by-sea"]
        result = parse_input(lines)
        expected_result = [{2: "airborne", 4: "by-sea"},
                        {3: "airborne"},
                        {0: "by-sea", 2: "airborne", 4: "by-sea"}]
        self.assertEqual(result, expected_result)

class TestHelper(unittest.TestCase):

    def test_itinerary_from_number(self):

        # Test case 1
        k = 2
        base_itienary = ["by-sea", "by-sea", "by-sea", "by-sea"]
        result = itinerary_from_number(k, base_itienary)
        expected_result = ["by-sea", "by-sea", "airborne", "by-sea"]
        self.assertEqual(result, expected_result)

        # Test case 2
        k = 15
        base_itienary = ["by-sea", "by-sea", "by-sea", "by-sea", "by-sea"]
        result = itinerary_from_number(k, base_itienary)
        expected_result = ["by-sea", "airborne", "airborne", "airborne", "airborne"]
        self.assertEqual(result, expected_result)


    def test_check_can_satisfy(self):

        # Test case 1
        d1 = {0: 'by-sea', 2: 'by-sea', 3: 'by-sea'} 
        d2 = {0: 'airborne', 1: 'airborne', 2: 'airborne', 3: 'airborne', 4: 'airborne', 5: 'by-sea'}
        result = check_can_satisfy(d1, d2)
        expected_result = False
        self.assertEqual(result, expected_result)

        # Test case 2
        d1 = {0: 'airborne', 3: 'by-sea'} 
        d2 = {0: 'by_sea', 1: 'airborne', 2: 'airborne', 3: 'by-sea', 4: 'airborne', 5: 'airborne'}
        result = check_can_satisfy(d1, d2)
        expected_result = True
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()