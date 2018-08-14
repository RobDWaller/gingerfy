from gingerfy.gingerfied import Gingerfied

class Gingerfy:

    def __init__(self): pass

    def fix(self, string):

        broken = string

        fix = string.replace("Blonde", "Ginger")

        fixes = ["Blonde"]

        return Gingerfied(fix, broken, fixes)
