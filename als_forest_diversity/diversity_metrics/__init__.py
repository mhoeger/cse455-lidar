from .canopy_cover import *
from .canopy_height import *
from .entropy import *
from .gap_fraction import *
from .height import *
from .rumple import *
from .rugosity import *
from .vai import *
from .vci import *
from als_forest_diversity.data.rasterize import to_2d_matrix

def all_diversity_metrics(chm_array, chm = None):
    if chm is None:
        chm = to_2d_matrix(chm_array)

    summary = {}
    summary["mean canopy height"] = mean_outer_canopy_ht(chm)
    summary["max canopy height"] = max_canopy_ht(chm)
    summary["rumple index"] = rumple_index(chm)
    summary["deepgaps"] = deepgaps(chm)
    summary["deepgap fraction"] = deepgap_fraction(chm)
    summary["cover fraction"] = cover_fraction(chm)
    summary["top rugosity"] = rugosity(chm)
    summary["height standard deviation"] = height_sd(chm_array)
    summary["height complexity"] = height_complexity(chm_array)
    summary["entropy"] = entropy(chm_array)
    summary["gap fraction profile"] = gap_fraction_mean(chm_array)
    summary["vegetation area index"] = vai(chm_array)
    summary["vertical complexity index"] = vci(chm_array)

    return summary

