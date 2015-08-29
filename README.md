# Optimization Practice

Hello! This project should help you brush up on some general
optimization tricks, as well as some of Python's performance and
memory characteristics.

# Instructions

Clone this folder into your local machine. Make sure you have Python 3
installed, either through your Operating System's package manager, or
through the [python website](https://www.python.org/downloads/).

One of the core functionalities of KA Lite is fetching and downloading
videos. The `download_videos_and_images.py` simulates part of that
functionality by reading through the items in `contents.json` and
extracting the download urls for each item in there.

You can run the script through your terminal:
```bash
python3 download_videos_and_images.py
```

Your task is to determine the memory and CPU performance
characteristics of the given script. Specifically, you have to answer
the following questions:


1. What is the average runtime of the script? (The [timeit module](https://docs.python.org/3.3/library/timeit.html) may be of help)
1. What is the highest memory usage of the program?
1. Which data type occupies the most memory? (The modules detailed [in this blog post](http://chase-seibert.github.io/blog/2013/08/03/diagnosing-memory-leaks-python.html) will be helpful)
1. Which parts can we optimize to reduce memory usage and runtime?
   Suggest at least 3 ways we can optimize this script.


You can optionally send in a rewritten script as well to show how
you'd implement your ideas.

# Sending your answers

Post your answers to the questions to https://gist.github.com/, with
the first text file containing the answers to each question, along
with an explanation and output of the profiling tool of your
choice. If you chose to rewrite the script to be more performant, you
can add that as the second file. Send the github gist link to the
person who sent this repo link to you.

That's it! Good luck and happy debugging!
