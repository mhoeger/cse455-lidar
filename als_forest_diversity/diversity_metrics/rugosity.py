import numpy as np

def rugosity(chm):
    """Standard deviation of out canopy heights in 1 m2 of plot"""
    return np.nanstd(chm)
