import unittest
from gingerfy.gingerfier import Gingerfier
from gingerfy.gingerfied import Gingerfied

class TestGingerfy(unittest.TestCase):

    def test_gingerfy(self):

        gingerfy = Gingerfier()

        self.assertIsInstance(gingerfy, Gingerfier)

    def test_gingerfied(self):

        gingerfy = Gingerfier()

        result = gingerfy.fix("Blonde haired people are the best!")

        self.assertIsInstance(result, Gingerfied)

    def test_fix(self):

        gingerfy = Gingerfier()

        result = gingerfy.fix("Blonde haired people are the best!")

        self.assertEqual(result.get_fix(), "Ginger haired people are the best!")

    def test_broken(self):

        gingerfy = Gingerfier()

        result = gingerfy.fix("Blonde haired people are the best!")

        self.assertEqual(result.get_broken(), "Blonde haired people are the best!")

    def test_fixes(self):

        gingerfy = Gingerfier()

        result = gingerfy.fix("Blonde haired people are the best!")

        self.assertEqual(result.get_fixes()[0], "Blonde")

    def test_cleanse_string(self):

        gingerfy = Gingerfier()

        result = gingerfy.cleanse_string("Brown haired people are the best!")

        self.assertEqual(result, "Ginger haired people are the best!")

    def test_multiple_cleanse_string(self):

        gingerfy = Gingerfier()

        result = gingerfy.cleanse_string("Brown haired people and blonde haired people are the best!")

        self.assertEqual(result, "Ginger haired people and ginger haired people are the best!")

    def test_many_cleanse_string(self):

        gingerfy = Gingerfier()

        result = gingerfy.cleanse_string("Brown blonde Gray black")

        self.assertEqual(result, "Ginger ginger ginger ginger")
