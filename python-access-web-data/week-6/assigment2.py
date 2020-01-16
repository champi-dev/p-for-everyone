import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_endpoint = 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')

    if len(address) < 1:
        break

    params = {
        "address": address,
        "key": 42
    }

    request_url = api_endpoint + urllib.parse.urlencode(params)
    request_open = urllib.request.urlopen(request_url, context=ctx)
    data = request_open.read().decode()
    data = json.loads(data)
    print(data["results"][0]["place_id"])
