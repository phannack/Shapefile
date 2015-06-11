__author__ = 'apple'

## Get Shapefile Fields - Get the user defined fields

from osgeo import ogr

daShapefile = r"ne1.shp"

dataSource = ogr.Open(daShapefile)
daLayer = dataSource.GetLayer(0)
layerDefinition = daLayer.GetLayerDefn()


for i in range(layerDefinition.GetFieldCount()):
    print layerDefinition.GetFieldDefn(i).GetName()