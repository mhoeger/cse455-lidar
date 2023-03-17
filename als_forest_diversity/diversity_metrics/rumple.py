from math import sqrt
from als_forest_diversity.diversity_metrics.utils import is_nan
import numpy as np


def _get_value(chm, i, j):
    if i < 0:
        i = 0
    if j < 0:
        j = 0
    if i >= len(chm):
        i = len(chm) - 1
    if j >= len(chm[0]):
        j = len(chm[0]) - 1
    return chm[i][j]

def _get_edge_length(i_1, j_1, i_2, j_2, chm, res):
    # horizontal distance
    if i_1 == i_2 or j_1 == j_2:
        a = res
    else:
        a = sqrt(res ** 2 + res ** 2)
    # elevation difference
    b = _get_value(chm, i_1, j_1) - _get_value(chm, i_2, j_2)
    # surface length
    c = sqrt(a**2 + b**2)
    return c / 2.0

def _get_triangle_area(i_1, j_1, i_2, j_2, i_3, j_3, chm, res):
    if is_nan(_get_value(chm, i_1, j_1)) or is_nan(_get_value(chm, i_2, j_2)) or is_nan(_get_value(chm, i_3, j_3)):
        return 1/8.0 * res ** 2

    edge_1_2 = _get_edge_length(i_1, j_1, i_2, j_2, chm, res)
    edge_1_3 = _get_edge_length(i_1, j_1, i_3, j_3, chm, res)
    edge_2_3 = _get_edge_length(i_2, j_2, i_3, j_3, chm, res)

    s = (edge_1_2 + edge_1_3 + edge_2_3) / 2.0
    area = sqrt(s * (s - edge_1_2) * (s - edge_1_3) * (s - edge_2_3))
    return area

def _get_surface_area(chm, res):
    """
    Area of canopy surface
    
    Reference:
    Jenness, J. S. (2004). Calculating landscape surface area from digital elevation models.
    Wildlife Society Bulletin, 32(3), 829-839.
    """
    total_area = 0
    for i in range(len(chm)):
        for j in range(len(chm[0])):
            if not is_nan(chm[i][j]):
                area = 0
                area += _get_triangle_area(i, j, i-1, j-1, i-1, j, chm, res)
                area += _get_triangle_area(i, j, i-1, j, i-1, j+1, chm, res)
                area += _get_triangle_area(i, j, i, j-1, i-1, j-1, chm, res)
                area += _get_triangle_area(i, j, i, j+1, i-1, j+1, chm, res)
                area += _get_triangle_area(i, j, i+1, j-1, i, j-1, chm, res)
                area += _get_triangle_area(i, j, i+1, j-1, i+1, j, chm, res)
                area += _get_triangle_area(i, j, i+1, j+1, i+1, j, chm, res)
                area += _get_triangle_area(i, j, i+1, j+1, i, j+1, chm, res)
                total_area += area
    return total_area

def _get_2d_area(chm, res):
    """Plot area"""
    return np.sum(~np.isnan(chm))* res ** 2

def rumple_index(chm):
    """
    Area of canopy surface relative to plot area

    Reference:
    https://github.com/r-lidar/lidR/blob/1a71a4a166cd453ec1b5ec933cc9056bce7e88af/R/metrics_stdmetrics.R
    """
    res = 1
    area_3d = _get_surface_area(chm, res)
    area_2d = _get_2d_area(chm, res)
    return area_3d / area_2d
