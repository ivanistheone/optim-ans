#!/usr/bin/env python3

# The goal of this script is to download all the mp4 and png
# data for each content.

import json
import urllib.request


# First, read the contents file into memory, then parse it into json.
with open("contents.json") as f:
    contents_str = f.read()
    contents = json.loads(contents_str)


# Then, loop over each content, and get its mp4 and png values.
print("Extracting mp4 and png links.")
mp4_links = []
png_links = []
for content in contents.values():
    mp4 = content["download_urls"]["mp4"]
    png = content["download_urls"]["png"]
    png_links.append(png)
    mp4_links.append(mp4)


# For the sake of runtime and reproducibility let's just download the
# first 10 links. You can reduce this if you want.
LIMIT = 10

# Now, download each mp4 link.
print("Downloading mp4 links.")
for mp4 in mp4_links[:LIMIT]:
    r = urllib.request.urlopen(mp4)
    # Let's not save the file to avoid cluttering our filesystem.


# Now, download each png link.
print("Downloading png links.")
for png in png_links[:LIMIT]:
    r = urllib.request.urlopen(png)
    # Let's not save the file to avoid cluttering our filesystem.
