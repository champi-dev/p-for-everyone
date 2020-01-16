import ssl
import json
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
data = urlopen(url, context=ctx).read().decode()
data = json.loads(data)

comments_sum = 0
for comment in data["comments"]:
    comments_sum += comment["count"]

print(comments_sum)
