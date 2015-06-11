__author__ = 'apple'

import ogr
cnt = ogr.GetDriverCount()
formatsList = []  # Empty List

for i in range(cnt):
    driver = ogr.GetDriver(i)
    driverName = driver.GetName()
    if not driverName in formatsList:
        formatsList.append(driverName)

formatsList.sort() # Sorting the messy list of ogr drivers

for i in formatsList:
    print i
