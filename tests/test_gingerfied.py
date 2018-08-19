import unittest
from gingerfy.src.gingerfied import Gingerfied

class TestGingerfied(unittest.TestCase):

    def test_gingerfy(self):

        fixes = ["colours", "fixed"]

        gingerfied = Gingerfied("Fixed String", "Broken String", fixes)

        self.assertIsInstance(gingerfied, Gingerfied)

    def test_get_fix(self):

        fixes = ["colours", "fixed"]

        gingerfied = Gingerfied("Fixed String", "Broken String", fixes)

        self.assertEqual(gingerfied.get_fix(), "Fixed String")

    def test_get_broken(self):

        fixes = ["colours", "fixed"]

        gingerfied = Gingerfied("Fixed String", "Broken String", fixes)

        self.assertEqual(gingerfied.get_broken(), "Broken String")

    def test_get_fixes(self):

        fixes = ["colours", "fixed"]

        gingerfied = Gingerfied("Fixed String", "Broken String", fixes)

        self.assertEqual(gingerfied.get_fixes()[0], "colours")
        self.assertEqual(gingerfied.get_fixes()[1], "fixed")
