
from arcgis.gis import GIS

x = input()

gis = GIS()
map = gis.map(x)
print(map)