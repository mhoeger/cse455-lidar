import logging
import pdal
import geopandas
from als_forest_diversity.config import HIGH_NOISE_CLASS, LOW_NOISE_CLASS, SMRF_PARAMS
from typing import Dict
from math import ceil, floor
from statistics import mean
import numpy as np


logger = logging.getLogger(__name__)

def get_chm_points(copc_file, polygon_file=None):
    # First create an empty PDAL pipeline
    pipeline = pdal.Pipeline()

    # Read whole file or part of the file
    if polygon_file:
        pipeline |= pdal.Reader(
            filename=copc_file,
            type="readers.copc",
            polygon=geopandas.read_file(polygon_file).geometry.to_wkt()[0]
        )
    else:
        pipeline |= pdal.Reader(
            filename=copc_file,
            type="readers.copc",
        )

    # Filter outliers
    pipeline |= pdal.Filter.outlier(
        method="statistical",
        mean_k=12,
        multiplier=2.2,
    )

    # Remove outliers + pre-classified noise
    pipeline |= pdal.Filter.range(limits=f"Classification![{LOW_NOISE_CLASS}:{LOW_NOISE_CLASS}]") 
    pipeline |= pdal.Filter.range(limits=f"Classification![{HIGH_NOISE_CLASS}:{HIGH_NOISE_CLASS}]") 
    
    # Classify ground points
    pipeline |= pdal.Filter.elm()
    pipeline |= pdal.Filter.smrf(**SMRF_PARAMS)

    # Get height above ground
    pipeline |= pdal.Filter.hag_nn() # Use Nearest Neighbors for detecting ground
    pipeline |= pdal.Filter.ferry(dimensions="HeightAboveGround=>Z")
    pipeline |= pdal.Filter.range(limits="Z[0:]")

    # Run pipeline
    small_pc_execution = pipeline.execute() # Returns count of points

    logger.info(f"Read {small_pc_execution} points from {copc_file}")
    
    # Returns points as numpy array
    return pipeline.arrays

def _to_grid(pc_array, aggregation_function, bin_size: int = 1):
    xs = pc_array[0]["X"]
    ys = pc_array[0]["Y"]
    zs = pc_array[0]["Z"]

    points = {}
    minx = floor(min(xs))
    maxx = ceil(max(xs))
    miny = floor(min(ys))
    maxy = ceil(max(ys))

    for i in range(0, len(xs)):
        x = floor(xs[i])
        y = floor(ys[i])
        if points.get(x):
            if points[x].get(y):
                points[x][y].append(zs[i])
            else:
                points[x][y] = [zs[i]]
        else:
            points[x] = { y: [zs[i]] }

    matrix = [np.nan] * (maxx - minx)
    for i in range(minx, maxx):
        matrix[i - minx] = [np.nan] * (maxy - miny)
        for j in range(miny, maxy):
            values = points.get(i, {}).get(j)
            if values:
                aggregate_height = aggregation_function(values)
                matrix[i - minx][j - miny] = aggregate_height

    return matrix

def to_2d_matrix(pc_array, bin_size: int=1):
    return _to_grid(pc_array, np.nanmean, bin_size)

def to_2d_sd_matrix(pc_array, bin_size: int=1):
    return _to_grid(pc_array, np.nanstd, bin_size)

def _gap_fraction_3m(values):
    count_over_3m = 0
    for value in values:
        if value > 3:
            count_over_3m += 1
    return count_over_3m / len(values)

def to_gap_fraction_matrix(pc_array, bin_size: int=1):
    return _to_grid(pc_array, _gap_fraction_3m, bin_size)