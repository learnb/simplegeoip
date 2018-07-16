import os
import simplegeoip
import geoip2.database

# Get the root dir of ip2geo module. Hack to ensure correct db path is used
#geoLibPath = os.path.dirname(simplegeoip.__file__) + "/"

_ip = "51.233.60.75"

#coords = simplegeoip.lookupIP(_ip, _dbPath=geoLibPath, _format="geojson")
coords = simplegeoip.lookupIP(_ip)
if(not coords):
    print "error: Failed to find coordinates for {0} ".format(_ip)
    sys.exit(2)
else:
    print(coords)
