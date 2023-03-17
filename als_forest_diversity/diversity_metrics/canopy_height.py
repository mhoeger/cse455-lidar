import numpy as np


def mean_outer_canopy_ht(chm):
    """Mean of maximum height in 1m2 grid of plot"""
    return np.nanmean(chm)

def max_canopy_ht(chm):
    """Maximum height within the plot area"""
    return np.nanmax(chm)