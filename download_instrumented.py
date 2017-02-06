#!/usr/bin/env python3

# The goal of this script is to download all the mp4 and png
# data for each content.

import imghdr
import logging
import json
import tempfile
import urllib.request

from pympler.asizeof import asizeof


logging.basicConfig(level=logging.ERROR)

# First, read the contents.json file into memory, then parse it.
with open("contents.json") as f:
    contents_str = f.read()
    contents = json.loads(contents_str)

# print memory usage 1
print('json data as text =', asizeof(contents_str)/1024, 'KB')
print('json data as dict =', asizeof(contents)/1024, 'KB')

# Then, loop over each content, and get its mp4 and png values.
logging.info("Extracting mp4 and png links.")
mp4_links = []
png_links = []
for content in contents.values():
    mp4 = content["download_urls"]["mp4"]
    png = content["download_urls"]["png"]
    png_links.append(png)
    mp4_links.append(mp4)


# print memory usage 2
print('mp4 links list =', asizeof(mp4_links)/1024, 'KB')
print('png links list =', asizeof(png_links)/1024, 'KB')

# For the sake of runtime and reproducibility let's just download the
# first 50 links. You can reduce this if you want.
LIMIT = 50


# Now, download each mp4 link.
logging.info("Downloading mp4 links.")
for mp4 in mp4_links[:LIMIT]:
    logging.info("Downloading {}".format(mp4))
    r = urllib.request.urlopen(mp4)
    # Let's not save the file to avoid cluttering our filesystem.

    # What's a fast and succinct way of detecting whether what we downloaded
    # was an MP4 file?


# Now, download each png link.
# However, we want to figure out if what we downloaded was a PNG file.
# If it's not a PNG file, then it should not be in the filesystem after
# this script.
logging.info("Downloading png links.")
for png in png_links[:LIMIT]:
    logging.info("Downloading {}".format(png))
    r = urllib.request.urlopen(png)

    # temporary file, so we don't clutter our filesystem.
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        contents = r.read()

        if imghdr.what(None, h=contents) != "png":
            logging.info("Image is not a PNG; not saving.")
        else:
            f.write(contents)
