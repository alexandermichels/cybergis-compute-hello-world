import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import random
import os
import webbrowser
import folium

print("THIS IS AN EXTRA SCRIPT THAT HOPEFULLY WILL RUN ON EXECUTION")

def make_random_gdf(lat, lon):
  # Define the number of points you want
  num_points = 100
  
  # Generate random points within a specified bounding box
  # Latitude between -90 and 90, Longitude between -180 and 180
  latitudes = [random.uniform(-lat, lat) for _ in range(num_points)]
  longitudes = [random.uniform(-lon, lon) for _ in range(num_points)]
  
  # Create Point geometries
  points = [Point(lon, lat) for lon, lat in zip(longitudes, latitudes)]
  
  # Create a GeoDataFrame
  gdf = gpd.GeoDataFrame(geometry=points)
  
  # Optionally, add more columns to the GeoDataFrame
  gdf['Value'] = [random.randint(1, 100) for _ in range(num_points)]
  
  gdf.head()  # Display the first few rows of the GeoDataFrame
  
  try:
    gdf = gdf.to_crs(epsg=4326)
  except Exception as e:
    gdf = gdf.set_crs("EPSG:4326", allow_override=False)
  try:
    print("Checkpoint1")
    m = gdf.explore(tiles='OpenStreetMap')
    m.save("map_visualization.html")
    filepath = "file://" + os.path.realpath("map_visualization.html")
    webbrowser.open_new_tab(filepath)
    print("Checkpoint2")
  except Exception as e:
    print("Failed to display map, encountered error")
    print(e)
  return gdf

gdf1 = make_random_gdf(45, 90)
gdf2 = make_random_gdf(90, 180)
RESULTS_FOLDER = os.getcwd()
gdf1.to_file(os.path.join(RESULTS_FOLDER, "result.shp"))
gdf2.to_file(os.path.join(RESULTS_FOLDER, "result.geojson"), driver='GeoJSON')
print("Saved result to result.shp, result.geojson")
