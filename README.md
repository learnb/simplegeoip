# SimpleGeoIp

Uses geoip2 package to read coordinates from a MaxMind GeoLite2 database.

For more information about geoip2 see their documentation: https://geoip2.readthedocs.io/en/latest/

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

_ip = "51.233.60.75"

coords = simplegeoip.lookupIP(_ip)
```
