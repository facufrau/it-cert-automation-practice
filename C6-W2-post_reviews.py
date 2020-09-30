#! /usr/bin/env python3
#Second assignment - convert txt to a dictionary and post too a webpage.
#Using requests and post method.

import os
import requests

files = os.listdir("/data/feedback")
url = 'http://34.122.55.140/feedback/'

for f in files:
    feedback = {}
    name = "/data/feedback/" + f
    with open(name) as file:
        lines = file.readlines()
        feedback["title"] = lines[0]
        feedback["name"] = lines[1]
        feedback["date"] = lines[2]
        feedback["feedback"] = lines[3]

    post = requests.post(url, json=feedback)
    if post.status_code == 201:
        print('Post ok for file: ' +  name)
    else:
        print('Error in posting file: ' + name)
        print(post.status_code)
