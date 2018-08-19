import unittest
from gingerfy import main
from gingerfy.src.gingerfied import Gingerfied

class TestGingerfy(unittest.TestCase):

    def test_fix(self):
        gingerfy = main

        result = gingerfy.fix("Blonde haired people are the best!")

        self.assertIsInstance(result, Gingerfied)
