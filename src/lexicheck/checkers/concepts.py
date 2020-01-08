from lexicheck.core import Check, CheckNotEmpty

class CheckNotEmptyConcepts(CheckNotEmpty):
    """Check for empty column parameters.csv"""
    table = 'ParameterTable'

