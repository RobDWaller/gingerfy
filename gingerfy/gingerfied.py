"""
Generated object for gingerfy module defines new fixed string, old unginger
string and the fixes that have been made.
"""
class Gingerfied(object):
    """Gingerfied class"""

    def __init__(self, fix, broken, fixes):
        """
        Constructor: consumes and sets fixed sentence, the old broken sentence
        and an array of the fixes.
        """

        self.fix = fix
        self.broken = broken
        self.fixes = fixes

    def get_fix(self):
        """Get the fixed sentence"""

        return self.fix

    def get_broken(self):
        """Get the original broken sentence"""

        return self.broken

    def get_fixes(self):
        """Get the array of fixes made"""

        return self.fixes
