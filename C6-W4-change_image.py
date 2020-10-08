#!/usr/bin/env python3
import os, sys
from PIL import Image

path = "supplier-data/images/"
files = os.listdir(path)

for file in files:
    if '.tiff' in file:
        image = Image.open(path + file).convert('RGB')
        new_image = image.resize((600,400))

        name = os.path.splitext(file)
        new_name = path + name[0] + '.jpeg'

        new_image.save(new_name, "JPEG")