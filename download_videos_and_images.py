#!/usr/bin/env python3

# The goal of this script is to download all the mp4 and png
# data for each content.

import imghdr
import logging
import json
import tempfile
import urllib.request

import magic


logging.basicConfig(level=logging.INFO)

# First, read the contents.json file into memory, then parse it.
with open("contents.json") as f:
    contents = json.load(f)


# Then, loop over each content, and get its mp4 and png values.
logging.info("Extracting mp4 and png links.")
mp4_links = []
png_links = []
for content in contents.values():
    mp4 = content["download_urls"]["mp4"]
    png = content["download_urls"]["png"]
    png_links.append(png)
    mp4_links.append(mp4)


# For the sake of runtime and reproducibility let's just download the
# first 50 links. You can reduce this if you want.
LIMIT = 50


# Now, download each mp4 link.
logging.info("Downloading mp4 links.")
for mp4 in mp4_links[:LIMIT]:
    logging.info("Downloading {}".format(mp4))
    r = urllib.request.urlopen(mp4)

    video_header = r.read(1024)
    # Save downloaded file only if it is an MP4 file (determine based on header)
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as vf:
        if magic.from_buffer(video_header, mime=True) != "video/mp4":
            logging.info("File is not an MP4; not saving.")
        else:
            rest_of_video = r.read()
            vf.write(video_header + rest_of_video)


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
