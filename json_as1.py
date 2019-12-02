import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    count_list = list()
    total_sum = 0
    url = input('Enter URL: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    print('Retrieved', len(data), 'characters')

    info = json.loads(data)
    print(json.dumps(info, indent=4))

    temp_list = info["comments"]
    for item in temp_list:
        count_list.append(item["count"])
    for i in range(len(count_list)):
        count_list[i] = int(count_list[i])
    total_sum = sum(count_list)
    print(total_sum)
