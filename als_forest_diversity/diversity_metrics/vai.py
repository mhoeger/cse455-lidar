from math import log
from .gap_fraction import gap_fraction_profile


def vai(chm_array):
    """
    Vegetation area index, sum of leaf area density (LAD) values for all 1m horizontal slices

    References:
    https://github.com/r-lidar/lidR/blob/1a71a4a166cd453ec1b5ec933cc9056bce7e88af/R/metrics_stdmetrics.R#L593
    """
    gap_frac = gap_fraction_profile(chm_array)
    k = 0.5
    sum_lad = 0
    for item in gap_frac:
        if item != 0:
            leaf_area_density = -1*log(item) / k
            sum_lad += leaf_area_density

    return sum_lad
