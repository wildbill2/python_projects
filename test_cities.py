import unittest
from city_functions import get_formatted_city


class CityTestCase(unittest.TestCase):
    """Tests for city_functions.py."""


    def test_city_country(self):
        """Do names like 'Athens, Greece' work?"""
        formatted_city = get_formatted_city('athens', 'greece')
        self.assertEqual(formatted_city, 'Athens, Greece')

    def test_city_country_population(self):
        """Do names like 'Santiago, Chile population - 500000' work?"""
        formatted_city = get_formatted_city('santiago', 'chile', population=500000)
        self.assertEqual(formatted_city, 'Santiago, Chile - population 500000')


unittest.main()