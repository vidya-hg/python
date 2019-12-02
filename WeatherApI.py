import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 'b6907d289e10d714a6e88b30761fae22'
    serviceurl = 'https://samples.openweathermap.org/data/2.5/weather?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    q = input('Enter location: ')
    if len(q) < 1: break

    parms = dict()
    parms['q'] = q
    if api_key is not False: parms['appid'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if js is None:
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    print("Current weather in ", q)
    print("===============================")
    print(js['weather'][0]['description'])
    print("Temperature: ", js['main']['temp'])
    print("Min Temp: ", js['main']['temp_min'])
    print("Max Temp: ", js['main']['temp_max'])
    print("Humidity:", js['main']['humidity'])
    
