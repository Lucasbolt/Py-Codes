#!/usr/bin/python3
""" This modules takes an argument from the command line.
search for it on google and opens top results in different taps.
"""
import sys, bs4, webbrowser, requests as resquest

if len(sys.argv) > 1:
    arg = '+'.join(sys.argv[1:])
else:
    arg = '+'.join(input("Enter search argument: ").split())
res = resquest.get('https://google.com/search?q={}'.format(arg))
ns = bs4.BeautifulSoup(res.text, 'html5lib')
res = ns.select('a')
link_list = []
for links in res:
    link = links.get('href')
    if "url?q=" in link and not 'webcache' in link:
        link_list.append(link.split('url?q=')[1].split('&sa=U')[0])

for i in range(3):
    webbrowser.open(link_list[i])
