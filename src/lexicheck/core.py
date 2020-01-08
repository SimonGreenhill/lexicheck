from collections import Counter

class Check:
    def __init__(self, dataset, cldf):
        self.dataset = dataset
        self.cldf = cldf
        self.errors = []
        
    def check(self):
        pass
        

class CheckNotEmpty(Check):
    """Check if a given column in the CLDF file is all empty"""
    
    table = 'LanguageTable'
    
    def check(self):
        nonempty = Counter()
        for row in self.cldf[self.table]:
            nonempty.update([k for k in row if row[k] != ""])

        for k in row:
            if nonempty.get(k, 0) == 1:
                self.errors.append("Empty column %s in table %s" % (k, self.table))
        
        return len(self.errors) == 0