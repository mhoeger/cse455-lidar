import numpy as np
from als_forest_diversity.data import to_2d_sd_matrix


def height_sd(pc_array):
    """Standard deviation of heights within plot area"""
    zs = pc_array[0]["Z"]
    return np.nanmean(zs)

def height_complexity(pc_array):
    """
    Plot level- standard deviation of the standard
    deviation of heights within 1 m2 voxels in plot
    """
    chm_sd = to_2d_sd_matrix(pc_array)
    return np.nanstd(chm_sd)

