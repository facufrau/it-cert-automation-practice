#! /usr/bin/env python3
import os, sys
import requests
import json

txt_path = "supplier-data/descriptions/"
txt_files = os.listdir(txt_path)

img_path = "supplier-data/images/"
img_files = os.listdir(img_path)

url = "http://34.70.10.143/fruits/"

for file in txt_files:
    if file.endswith(".txt"):
        #Get prefix for adding image corresponding to description.
        prefix = file.replace('.txt', '')

        with open(txt_path + file) as f:
            lines = f.readlines()
            fruit_dict = {}

            fruit_dict["name"] = lines[0]
            fruit_dict["weight"] = int(lines[1].replace(' lbs', ''))
            fruit_dict["description"] = lines[2]
            fruit_dict["image_name"] = prefix + '.jpeg'

            post = requests.post(url, json=fruit_dict)
            if post.status_code == 201:
                print('Post ok for file: ' + file)
            else:
                print('Error in posting file: ' + file)
                print(post.status_code)
