__author__ = 'apple'


from osgeo import ogr
import os

shapefile = "ne1.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()

layer.SetAttributeFilter("RAI = '0'") # filter by

for feature in layer:
    print feature.GetField("LU_CODE")