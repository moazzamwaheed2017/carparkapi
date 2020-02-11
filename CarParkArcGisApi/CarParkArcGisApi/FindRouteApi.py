
from arcgis.gis import GIS

user_name = 'arcgis_python'
password = 'P@ssword123'
gis = GIS('https://www.arcgis.com', user_name, password)

address_1 = input()

search_result = gis.content.search(address_1, "feature collection", max_items=1)

if len(search_result) == 0:
    print("list is empty")
else:    
    search_item = search_result[0]
    search_item

    map1 = gis.map(address_1)
    map1

    map1.add_layer(search_item)

    search_fc = search_item.layers[3]

    from arcgis.features import find_locations

    trace1 = find_locations.trace_downstream(search_fc)

    map1.add_layer(trace1)