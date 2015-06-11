__author__ = 'apple'

#Get Geometry from each Feature in a Layer

from osgeo import ogr
import os

shapefile = "ne1.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()

for feature in layer:
    geom = feature.GetGeometryRef()
    print geom.Centroid().ExportToWkt()

