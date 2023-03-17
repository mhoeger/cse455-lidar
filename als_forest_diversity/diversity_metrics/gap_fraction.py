import numpy as np
from als_forest_diversity.diversity_metrics.utils import count_heights


def gap_fraction_profile(pc_array):
    """
    Distribution of gaps in the point cloud 3 m above the ground

    References:
    https://github.com/r-lidar/lidR/blob/1a71a4a166cd453ec1b5ec933cc9056bce7e88af/R/metrics_stdmetrics.R#L557
    Bouvier, M., Durrieu, S., Fournier, R. a, & Renaud, J. (2015).  Generalizing predictive
    models of forest inventory attributes using an area-based approach with airborne las data. Remote
    Sensing of Environment, 156, 322-334. http://doi.org/10.1016/j.rse.2014.10.004
    """
    height_counts = count_heights(pc_array)
    normalized_height_counts = height_counts / np.sum(height_counts)
    np.append(normalized_height_counts, 0)
    cs = np.cumsum(normalized_height_counts, dtype=float)

    diff_ratio = []
    for i in range(1, len(cs)):
        diff_ratio.append(cs[i - 1] / cs[i])
    # remove last element
    diff_ratio.pop(-1)
    # only return buckets for items > 3m
    return diff_ratio[3:]

def gap_fraction_mean(pc_array):
    gapfrac = gap_fraction_profile(pc_array)
    return np.mean(gapfrac)
