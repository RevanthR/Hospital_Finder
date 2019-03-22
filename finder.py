from math import cos, sin, sqrt, atan2, radians
import csv
import geocoder
g=geocoder.ip('me')
location=g.latlng

R=6373.0

lat1 = radians(location[0])
lon1 = radians(location[1])
lat2 = radians(52.406374)
lon2 = radians(16.9251681)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)
print("Should be:", 278.546, "km")