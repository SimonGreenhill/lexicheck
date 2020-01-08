from lexicheck.core import Check


class CheckCLDFValid(Check):
    """Check if CLDF is valid"""
    def check(self):
        valid = self.cldf.validate()
        if not valid:
            self.errors.append('CLDF is invalid!')
            return not valid
        return valid
