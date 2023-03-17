import numpy as np
from math import isnan, ceil, floor


def is_nan(x):
    return  x is np.nan or isnan(x)

def count_heights(pc_array, interval=1, zmax=None):
    zs = pc_array[0]["Z"]
    if zmax is None:
        zmax = ceil(np.nanmax(zs))
    height_counts = [0] * zmax
    for z in zs:
        if not is_nan(z):
            bucket = floor(z)
            if bucket < 0:
                bucket = 0
            height_counts[bucket] += 1
    return height_counts