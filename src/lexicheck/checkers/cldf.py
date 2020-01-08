
def check_cldf_valid(dataset):
    """Check if CLDF is valid"""
    cldf = dataset.cldf_reader()
    return cldf.validate()
