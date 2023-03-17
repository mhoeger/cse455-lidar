from .entropy import entropy
import numpy as np
from math import ceil


def vci(chm_array):
    # set zmax comfortably above maximum canopy height
    return entropy(chm_array, zmax=100)