import geocoder
g=geocoder.ip('me')

location=g.latlng
print(location)