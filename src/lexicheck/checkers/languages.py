from lexicheck.core import Check, CheckNotEmpty

class CheckNotEmptyLanguages(CheckNotEmpty):
    """Check for empty column in languages.csv"""
    pass


class CheckGlottocodes(Check):
    """Check if Glottocodes are valid (simple)"""
    def check(self):
        for lang in self.dataset.languages:
            gc = lang.get("Glottocode", "")
            if len(gc) not in (0, 8):
                self.errors.append("Glottocode for language %s in ./etc/languages.csv is invalid" % lang.get("ID"))
        return len(self.errors) == 0



# TODO check bookmarking glottocodes etc