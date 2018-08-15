import unittest
from gingerfy import Gingerfy
from gingerfy import Gingerfied

class TestGingerfy(unittest.TestCase):

    def test_gingerfy(self):

        gingerfy = Gingerfy()

        self.assertIsInstance(gingerfy, Gingerfy)

    def test_gingerfied(self):

        gingerfy = Gingerfy()

        result = gingerfy.fix("Blonde haired people are the best!")

        self.assertIsInstance(result, Gingerfied)

    def test_fix(self):

        gingerfy = Gingerfy()

        result = gingerfy.fix("Blonde haired people are the best!")

        self.assertEqual(result.getFix(), "Ginger haired people are the best!")

    def test_broken(self):

        gingerfy = Gingerfy()

        result = gingerfy.fix("Blonde haired people are the best!")

        self.assertEqual(result.getBroken(), "Blonde haired people are the best!")

    def test_fixes(self):

        gingerfy = Gingerfy()

        result = gingerfy.fix("Blonde haired people are the best!")

        self.assertEqual(result.getFixes()[0], "Blonde")

    def test_cleanse_string(self):

        gingerfy = Gingerfy()

        result = gingerfy.cleanseString("Brown haired people are the best!")

        self.assertEqual(result, "Ginger haired people are the best!")

    def test_multiple_cleanse_string(self):

        gingerfy = Gingerfy()

        result = gingerfy.cleanseString("Brown haired people and blonde haired people are the best!")

        self.assertEqual(result, "Ginger haired people and ginger haired people are the best!")

    def test_many_cleanse_string(self):

        gingerfy = Gingerfy()

        result = gingerfy.cleanseString("Brown blonde Gray black")

        self.assertEqual(result, "Ginger ginger ginger ginger")
