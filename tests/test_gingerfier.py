import unittest
from src.gingerfier import Gingerfier
from src.gingerfied import Gingerfied

class TestGingerfier(unittest.TestCase):

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

    def test_many_fixes(self):

        gingerfy = Gingerfier()

        result = gingerfy.fix("Black and gray haired people are the best!")

        self.assertEqual(len(result.get_fixes()), 2)
        self.assertTrue("Black" in result.get_fixes())
        self.assertTrue("gray" in result.get_fixes())

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

    def test_create_fixes_list(self):

        gingerfy = Gingerfier()

        result = gingerfy.create_fixes_list("Brown haired people and blonde haired people are the best!")

        self.assertEqual(len(result), 2)
        self.assertTrue("Brown" in result)
        self.assertTrue("blonde" in result)

    def test_many_create_fixes_list(self):

        gingerfy = Gingerfier()

        result = gingerfy.create_fixes_list("Brown Blonde Gray black")

        self.assertEqual(len(result), 4)
        self.assertTrue("Brown" in result)
        self.assertTrue("Blonde" in result)
        self.assertTrue("Gray" in result)
        self.assertTrue("black" in result)
        self.assertFalse("Black" in result)
        self.assertFalse("gray" in result)
