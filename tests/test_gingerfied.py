import unittest
from gingerfy import Gingerfied

class TestGingerfied(unittest.TestCase):

    def test_gingerfy(self):

        fixes = ["colours", "fixed"]

        gingerfied = Gingerfied("Fixed String", "Broken String", fixes)

        self.assertIsInstance(gingerfied, Gingerfied)

    def test_get_fix(self):

        fixes = ["colours", "fixed"]

        gingerfied = Gingerfied("Fixed String", "Broken String", fixes)

        self.assertEqual(gingerfied.getFix(), "Fixed String")

    def test_get_broken(self):

        fixes = ["colours", "fixed"]

        gingerfied = Gingerfied("Fixed String", "Broken String", fixes)

        self.assertEqual(gingerfied.getBroken(), "Broken String")

    def test_get_fixes(self):

        fixes = ["colours", "fixed"]

        gingerfied = Gingerfied("Fixed String", "Broken String", fixes)

        self.assertEqual(gingerfied.getFixes()[0], "colours")
        self.assertEqual(gingerfied.getFixes()[1], "fixed")
