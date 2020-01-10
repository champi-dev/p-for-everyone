import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

repeat_times = 7
tag_position = 18
starter_url = 'http://py4e-data.dr-chuck.net/known_by_Brad.html'
current_tag = None

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_current_tag(url):
    if url is None:
        url = starter_url

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags[tag_position - 1].get('href', None)


while repeat_times > 0:
    repeat_times -= 1
    current_tag = get_current_tag(current_tag)
    print(current_tag)
