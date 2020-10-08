#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

path = "supplier-data/images/"
files = os.listdir(path)

for file in files:
    if '.jpeg' in file:
        filename = path + file
        with open(filename, 'rb') as opened:
            try:
                r = requests.post(url, files={'file': opened})
                print("File {} posted OK!".format(filename))
            except:
                print("Error while posting request")
