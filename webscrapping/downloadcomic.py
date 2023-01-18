#!/usr/bin/python3
"""Downloads comic pictures from xkcd.com"""
import requests, os
from bs4 import BeautifulSoup


url = 'http://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()
    ns = BeautifulSoup(res.text)
    res = ns.select('#comic img')

    comicurl = res[0].get('src')
    if not comicurl.startswith('http'):
        comicurl = 'https://xkcd.com' + comicurl
    print("Downloading image {}...".format(comicurl))
    res = requests.get(comicurl)
    res.raise_for_status()
    imagefile = open(os.path.join('xkcd', os.path.basename(comicurl)), 'wb')
    for chunks in res.iter_content(10000):
        imagefile.write(chunks)
    imagefile.close()
    prevl =  ns.select("a[rel = 'prev']")[0]
    url = 'https://xkcd.com/' + prevl.get('href')

print('Done.')
