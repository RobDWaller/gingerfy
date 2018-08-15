from gingerfy.gingerfied import Gingerfied
from gingerfy.unginger import colours

class Gingerfy:

    def __init__(self): pass

    def fix(self, string):

        broken = string

        fix = self.cleanseString(string)

        fixes = ["Blonde"]

        return Gingerfied(fix, broken, fixes)

    def cleanseString(self, string):

        result = string

        for colour in colours:
            result = result.replace(colour, "ginger")

        if result != string:
            return result.capitalize()
        else:
            return self.cleanseString(result)
