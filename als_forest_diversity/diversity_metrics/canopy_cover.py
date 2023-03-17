import numpy as np


def _valid_count(chm):
    return np.count_nonzero(~np.isnan(chm))

def _nan_count(chm):
    return np.count_nonzero(np.isnan(chm))

def _zero_count(chm):
    return (len(chm) * len(chm[0])) - np.count_nonzero(chm)

def deepgaps(chm):
    """The number of 1 m2 canopy gaps in the plot"""
    return _zero_count(chm)

def deepgap_fraction(chm):
    """Fraction of 1 m2 canopy gaps in the plot"""
    deepgap_count = deepgaps(chm)
    return deepgap_count / _valid_count(chm)

def cover_fraction(chm):
    """1 minus deep gap fraction"""
    return 1 - deepgap_fraction(chm)