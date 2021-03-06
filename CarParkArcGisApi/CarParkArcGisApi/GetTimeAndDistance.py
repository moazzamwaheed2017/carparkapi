
from copy import deepcopy
from datetime import datetime
from IPython.display import HTML

import json
import pandas as pd
from arcgis.gis import GIS
import arcgis.network as network
import arcgis.geocoding as geocoding

user_name = 'arcgis_python'
password = 'P@ssword123'
my_gis = GIS('https://www.arcgis.com', user_name, password)


route_service_url = my_gis.properties.helperServices.route.url
route_service_url

route_service = network.RouteLayer(route_service_url, gis=my_gis)
route_service

address_1 = input()
address_2 = input()

stop1_address = address_1
stop2_address = address_2

stop1_geocoded = geocoding.geocode(stop1_address)
stop2_geocoded = geocoding.geocode(stop2_address)

stops = '{0},{1}; {2},{3}'.format(stop1_geocoded[0]['attributes']['X'],
                                  stop1_geocoded[0]['attributes']['Y'],
                                  stop2_geocoded[0]['attributes']['X'],
                                  stop2_geocoded[0]['attributes']['Y'])

route_layer = network.RouteLayer(route_service_url, gis=my_gis)
result = route_layer.solve(stops=stops, return_directions=True, return_routes=True, 
                           output_lines='esriNAOutputLineNone', return_barriers=False, 
                           return_polygon_barriers=False, return_polyline_barriers=False)

travel_time = result['routes']['features'][0]['attributes']['Total_TravelTime']
print("Total travel time is {0:.2f} min".format(travel_time))

total_distance = result['routes']['features'][0]['attributes']['Total_Kilometers']
print("Total distance is {0:.2f} km".format(total_distance))
