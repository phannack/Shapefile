__author__ = 'apple'

# Get a Layer’s Capabilities

from osgeo import ogr

ds = ogr.Open("ShapefileTest/States/states.shp",0)


layer = ds.GetLayer()
capabilities = [
    ogr.OLCRandomRead,
    ogr.OLCSequentialWrite,
    ogr.OLCRandomWrite,
    ogr.OLCFastSpatialFilter,
    ogr.OLCFastFeatureCount,
    ogr.OLCFastGetExtent,
    ogr.OLCCreateField,
    ogr.OLCDeleteField,
    ogr.OLCReorderFields,
    ogr.OLCAlterFieldDefn,
    ogr.OLCTransactions,
    ogr.OLCDeleteFeature,
    ogr.OLCFastSetNextByIndex,
    ogr.OLCStringsAsUTF8,
    ogr.OLCIgnoreFields
]

print("Layer Capabilities:")
for cap in capabilities:
    print("  %s = %s" % (cap, layer.TestCapability(cap)))