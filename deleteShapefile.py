__author__ = 'apple'

from osgeo import ogr
import os

DriverName = "ESRI Shapefile"
FileName = 'ne1.shp' # Path Shapefile
driver = ogr.GetDriverByName(DriverName)
if os.path.exists(FileName):
     driver.DeleteDataSource(FileName)
