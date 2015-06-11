__author__ = 'apple'

# Get Shapefile Fields and Types - Get the user defined fields

from osgeo import ogr

daShapefile = r"ne1/ne1.shp" # Path your Shapefile

dataSource = ogr.Open(daShapefile)
daLayer = dataSource.GetLayer(0)
layerDefinition = daLayer.GetLayerDefn()


print "Name  -  Type  Width  Precision"
for i in range(layerDefinition.GetFieldCount()):
    fieldName =  layerDefinition.GetFieldDefn(i).GetName()
    fieldTypeCode = layerDefinition.GetFieldDefn(i).GetType()
    fieldType = layerDefinition.GetFieldDefn(i).GetFieldTypeName(fieldTypeCode)
    fieldWidth = layerDefinition.GetFieldDefn(i).GetWidth()
    GetPrecision = layerDefinition.GetFieldDefn(i).GetPrecision()

    print fieldName + " - " + fieldType+ " " + str(fieldWidth) + " " + str(GetPrecision)