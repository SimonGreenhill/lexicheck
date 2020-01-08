from lexicheck.core import Check, CheckNotEmpty

class CheckNotEmptyConcepts(CheckNotEmpty):
    """Check for empty column in parameters.csv"""
    table = 'ParameterTable'

