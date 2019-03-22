from math import cos, sin, sqrt, atan2, radians
import csv
import geocoder
import data
g=geocoder.ip('me')
location=g.latlng


R=6373.0
lat_list=data.lat
lon_list=data.lon
cur_lat = radians(location[0])
cur_lon = radians(location[1])


def distance(lat1,lon1,lat2,lon2):
	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	dist = R * c
	return dist
sug_lat=[]
sug_lon=[]
for i in range(len(lat_list)):
	dist=distance(cur_lat,cur_lon,radians(float(lat_list[i])),radians(float(lon_list[i])))
	if dist <= 15:
		sug_lat.append(lat_list[i])
		sug_lon.append(lon_list[i])


print(sug_lat)
print(sug_lon)

