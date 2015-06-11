__author__ = 'apple'

import os
from osgeo import ogr

shapefile = r"ShapefileTest/GIS_CensusTract_poly.shp" # Path Your Shapefile

driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()

for feature in layer:
    print feature.GetField("SOURCE_3") # Get field SOURCE_3 all feature
