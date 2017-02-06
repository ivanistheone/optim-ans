#!/bin/bash
#
# This script runs `download_videos_and_images.py` to measure the avg. runtim
#
COMMAND="python3 download_videos_and_images.py"
DATAFILE="perfdata/runtime_baseline.txt"


# Experiment data stored as a text file in perfdata/
if [ -f $DATAFILE ]; then
    rm $DATAFILE;
fi
touch $DATAFILE
echo "Runtime baseline expriment "$(date) >> $DATAFILE


echo "Running video download script 10 times (baseline)"
for i in {1..10}; do
    echo "run "$i" is under way..."
    /usr/bin/time -f "%e" $COMMAND >>$DATAFILE 2>&1
done

