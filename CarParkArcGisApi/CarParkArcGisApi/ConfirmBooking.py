my_gis.content.search('title: ArcGIS Online Directions and Routing Services Coverage type:Web Map owner:esri',
                      item_type='Web Map', outside_org=True)[0]

my_gis.content.search('title: World Traffic Map type:Web Map owner:esri',
                      item_type='Web Map', outside_org=True)[0]

route_layer = network.RouteLayer(route_service_url, gis=my_gis)
result = route_layer.solve(stops='''18.068598,59.329268; 18.068598,59.429268''',
                           return_directions=False, return_routes=True, 
                           output_lines='esriNAOutputLineNone',
                           return_barriers=False, return_polygon_barriers=False, 
                           return_polyline_barriers=False)

travel_time = result['routes']['features'][0]['attributes']['Total_TravelTime']
print("Total travel time is {0:.2f} min".format(travel_time))
