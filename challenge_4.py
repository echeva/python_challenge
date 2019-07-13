import urllib
import random
import requests
import re

new_url = 'nueva url'
new_result = 'nuevo resultado'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579'

for x in range(4000):
    result = urllib.request.urlopen(url)
    lines = result.readlines()
    if 'and the next nothing is' in str(lines) or str(lines) == '':
        print('lines',lines)
        numero = re.sub("\D", "", str(lines))
        print(numero)
    else:
        print(lines)
        new_result = str(result)
        new_url = str(url)
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(numero)

print("nuevo resultado", new_result)
print("nuevo url", new_url)