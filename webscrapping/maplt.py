#!/usr/bin/python3
import sys, webbrowser, pyperclip as clipboard

web_addr = 'https://www.google.com/maps/place/'
if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])
else:
    address = input('Please enter the location to display: ')
    address = '+'.join(address.split())
web_addr += address

webbrowser.open(web_addr)

