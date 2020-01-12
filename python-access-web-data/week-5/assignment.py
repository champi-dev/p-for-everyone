import ssl
import xml.etree.ElementTree as ET
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
xml = urlopen(url, context=ctx).read()

xml = ET.fromstring(xml)
tag_list = xml.findall('.//count')

sum_total = 0
for tag in tag_list:
    sum_total += int(tag.text)

print(sum_total)
