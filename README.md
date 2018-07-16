# SimpleGeoIp

Uses geoip2 package to read coordinates from a MaxMind GeoLite2 database.

## Dependencies

geoip2

```
$ pip install geoip2
```

## Basic Usage

```
import os
import simplegeoip
import geoip2.database

_ip = "128.182.160.117"

coords = simplegeoip.lookupIP(_ip)
```
