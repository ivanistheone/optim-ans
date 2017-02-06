Answers
=======
This file contains some possible answers to the optimization challenge posed in
https://github.com/fle-internal/optimization-starter-project
The data files can be found [here][10] and also available as an [excel file][11].



## What is the average runtime of the script?

The script takes on average **15 seconds** to process/download the first 50 videos.
This number was obtained using the bash script [`runtime.sh`][1], which runs the
download script 10 times.

The test was performed on a linux box (Debian Jessie 8.7) running in the
`ca-central-1` AWS region. Significantly longer runtimes can be expected for
slower internet connections.



## What is the highest memory usage of the program?

The maximum memory usage is **48.7 MB** as determined by taking samples of the
program's memory usage as reported by `ps` using the script [`runmem.sh`][2].

The script was run using Python 3.4.2 on a x86_64 GNU/Linux 3.16 kernel.



## Which data type occupies the most memory?

Using the package `Pympler` and an instrumented version of the download script
[`download_instrumented.py`][3], we can peek into the memory usage of the data
structures used in the script:

  - json data as text = 7779.4 KB   = asizeof(contents_str)
  - json data as dict = 19888.1 KB  = asizeof(contents)
  - mp4 links list = 1037.9 KB  = asizeof(mp4_links)
  - png links list = 1037.9 KB  = asizeof(png_links)

The largest data structure is the dictionary `contents` that is of size **~20 MB**.
This Python dictionary contains the parsed contents of the file `contents.json`.



## Which parts can we optimize to reduce memory usage and runtime? Suggest at least 3 ways we can optimize this script.

Given the observations above and the reasonable runtime and reasonable memory
usage of this download script, there is no need for major architecture changes.
Nevertheless, the following changes (shown below as commit diffs) would improve
the performance and reliability of this download script:

  - There is possibility to save around **7MB** of memory by not loading the json
    file as a string, but using `json.load` directly. See [this commit][4].
    The changes were confirmed to save memory.

  - As suggested in the comments, we can improve the reliability of the script by
    checking if the file we've downloaded is really an MP4 file. We can rely on
    the library `libmagic` wrapped through the package `python-magic` for this.
    See [this commit][5].

  - The calls to `urllib.request` can result in several possible exceptions,
    which the script needs to handle in order to ensure smooth operation.
    See [this commit][6].

Continuing in the spirit of reliability and usability, another improvement to the
script would be to write a "journal" of the script's current progress. For example,
the script could log the ids of all the successfully downloaded MP4 and PNG into
a files called `progress.log`. If the download script crashes, the download process
need not restart from the beginning---MP4 and PNG files already downloaded can be
skipped by looking into `progress.log`.

Indeed, it would make more sense to download the MP4 file and the PNG file for
each video at the same time rather than separately. A download "transaction" would
be finished whenever both MP4 file and PNG file are downloaded and saved to disk.


Further improvements could include:

  - If the data file `contents.json` grows over time and becomes too large to load
    and parse into memory at once, it is possible to use an iteration-based json
    parsing library like `ijson` (see https://github.com/isagalaev/ijson).
    This will remove the need to load the entire json data into memory upfront.



[1]: https://github.com/ivanistheone/optim-ans/blob/perfimpr/runtime.sh
[2]: https://github.com/ivanistheone/optim-ans/blob/perfimpr/runmem.sh
[3]: https://github.com/ivanistheone/optim-ans/blob/perfimpr/download_instrumented.py

[4]: https://github.com/ivanistheone/optim-ans/commit/51a6de80d5
[5]: https://github.com/ivanistheone/optim-ans/commit/3ad5345f4b
[6]: https://github.com/ivanistheone/optim-ans/commit/a652f1aeb0

[10]: https://github.com/ivanistheone/optim-ans/tree/perfimpr/perfdata
[11]: https://docs.google.com/spreadsheets/d/1M1x1ZqVR7hqdzgUtuaNVUJ0t-cbHAkvFTfvezUsyZiY/edit?usp=sharing

