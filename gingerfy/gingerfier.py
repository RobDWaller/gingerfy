"""
Takes a string, looks for unginger colours and cleanses them with the one true
colour, Ginger!
"""
from gingerfy.gingerfied import Gingerfied
from gingerfy.unginger import COLOURS

class Gingerfier(object):
    """Class String"""

    def fix(self, string):
        """Method String"""

        broken = string

        fix = self.cleanse_string(string)

        fixes = ["Blonde"]

        return Gingerfied(fix, broken, fixes)

    @classmethod
    def cleanse_string(cls, string):
        """Method String"""

        for colour in COLOURS:
            string = string.replace(colour, "ginger")

        return string.capitalize()
