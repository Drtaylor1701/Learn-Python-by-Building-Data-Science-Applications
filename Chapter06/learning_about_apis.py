#!/usr/bin/env python3
import requests
from time import sleep
base_url = 'https://nominatim.openstreetmap.org/search?'
def nominatim_geocode(address, format = 'json', limit = 1, **kwargs):
    '''thin wrapper around nominatim API, Documentation: https://wiki.openstreetmap.org/wiki
     /Nominatim#Parameters'''

    params = {
        'format':'json',
        'q': 'Eiffel Tower'
    }
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()

    sleep(1) #stops this from generating too many requests
    return response.json()

print(nominatim_geocode('Eiffel Tower'))
