import numpy as np
from math import log
from als_forest_diversity.diversity_metrics.utils import count_heights


def _remove_zeros(array):
    new_array = []
    for item in array:
        if item != 0:
            new_array.append(item)
    return new_array

def entropy(pc_array, zmax = None):
    """
    Diversity and evenness of heights within the plot

    References:
    https://github.com/r-lidar/lidR/blob/1a71a4a166cd453ec1b5ec933cc9056bce7e88af/R/metrics_stdmetrics.R#L634
    Pretzsch, H. (2008). Description and Analysis of Stand Structures. Springer Berlin Heidelberg. http://doi.org/10.1007/978-3-540-88307-4 (pages 279-280)
    Shannon, Claude E. (1948), "A mathematical theory of communication," Bell System Tech. Journal 27, 379-423, 623-656.
    """
    height_counts = count_heights(pc_array, zmax=zmax)
    normalized_height_counts = height_counts / np.sum(height_counts)
    p = _remove_zeros(normalized_height_counts)
    pref = [1.0 / len(normalized_height_counts)] * len(normalized_height_counts)
    # normalized entropy
    numerator = 0
    for p_i in p:
        numerator -= p_i * log(p_i)
    denominator = 0
    for pref_i in pref:
        denominator -= pref_i * log(pref_i)

    return numerator / denominator