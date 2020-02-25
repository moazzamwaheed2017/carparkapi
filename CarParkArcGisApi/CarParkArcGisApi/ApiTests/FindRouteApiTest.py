
from arcgis.gis import GIS

user_name = 'arcgis_python'
password = 'P@ssword123'
gis = GIS('https://www.arcgis.com', user_name, password)

address_1 = "777 Brockton Avenue, Abington MA 2351"

search_result = gis.content.search("title:"+address_1, item_type = "Web Map")

if len(search_result) == 0:
    print("list is empty")
else:    
    search_item = search_result[0]
    search_item

    map1 = gis.map(address_1)
    map1

