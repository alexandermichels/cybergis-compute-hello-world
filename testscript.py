import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import random
import os


print("THIS IS AN EXTRA SCRIPT THAT HOPEFULLY WILL RUN ON EXECUTION")


# Define the number of points you want
num_points = 100

# Generate random points within a specified bounding box
# Latitude between -90 and 90, Longitude between -180 and 180
latitudes = [random.uniform(-90, 90) for _ in range(num_points)]
longitudes = [random.uniform(-180, 180) for _ in range(num_points)]

# Create Point geometries
points = [Point(lon, lat) for lon, lat in zip(longitudes, latitudes)]

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(geometry=points)

# Optionally, add more columns to the GeoDataFrame
gdf['Value'] = [random.randint(1, 100) for _ in range(num_points)]

gdf.head()  # Display the first few rows of the GeoDataFrame

RESULTS_FOLDER = os.getcwd()
gdf.to_file(os.path.join(RESULTS_FOLDER, "result.shp"))
print("Saved result to result.shp")