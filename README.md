# SimpleGeoIp

Uses geoip2 package to read coordinates from a MaxMind GeoLite2 database.

## Dependencies

geoip2

```
$ pip install geoip2
```
## Installing

```
git clone https://github.com/learnb/simplegeoip.git
cd simplegeoip
pip install -r requirements.txt
```
## Downloading GeoLite2 Database

To download the database to the current directory:

```
sh ./download_geo_ip_db.sh
```

## Basic Usage

```
import os
import simplegeoip
import geoip2.database

_ip = "128.182.160.117"

coords = simplegeoip.lookupIP(_ip)
```
