import unittest
from src.bar import Bar

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("Blue Lagoon", [
            {"beers":["guiness", "stella", "tennants"]},
            {"spirits": ["vodka", "rum", "whisky"]}
            ])
    
    def test_bar_has_name(self):
        self.assertEqual("Blue Lagoon", self.bar.name)

    # def test_bar_has_guiness(self):
    #     self.assertEqual("Blue Lagoon", self.bar.drinks[1])

    bar1 = Bar("Blue Lagoon", [
            {"beers":["guiness", "stella", "tennants"]},
            {"spirits": ["vodka", "rum", "whisky"]}
            ])
    print(bar1.drinks[beers])