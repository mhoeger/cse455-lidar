LOW_NOISE_CLASS = 7
HIGH_NOISE_CLASS = 18

OUTLIER_PARAMS = {
    "method": "statistical",
    "mean_k": 12,
    "multiplier": 2.2,
}
SMRF_PARAMS = {
    "ignore": f"Classification[{LOW_NOISE_CLASS:d}:{LOW_NOISE_CLASS:d}]",
    "slope": 0.2,
    "window": 16,
    "threshold": 0.45,
    "scalar": 1.2,
}

# File locations
LOCAL_HARV_COPC = "/home/mariehoeger/Documents/repos/cse455-lidar/data/raw/NEON_D01_HARV_DP1_727000_4702000_classified_point_cloud_colorized.copc.laz"
LOCAL_TEAK_COPC = "/home/mariehoeger/Documents/repos/cse455-lidar/data/raw/NEON_D17_TEAK_DP1_316000_4091000_classified_point_cloud_colorized.copc.laz"
LOCAL_TEAK_GEOMETRY = "/home/mariehoeger/Documents/repos/cse455-lidar/data/teak-geometry.geojson"
LOCAL_HARV_GEOMETRY = "/home/mariehoeger/Documents/repos/cse455-lidar/data/harv-geometry.geojson"