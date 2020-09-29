#!/usr/bin/env python3
#First assignment - Scale and convert images using PIL
import os, glob
from PIL import Image

directory = "/home/student-01-cc5c389a6a7b/images/"

for filename in glob.glob("ic_*"):
    im = Image.open(filename).convert('RGB')

    new_im = im.rotate(270).resize((128,128))
    name = "/opt/icons/" + filename + ".jpg"
    new_im.save(name, "JPEG")
