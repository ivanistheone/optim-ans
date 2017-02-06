#!/bin/bash
#
# This script runs `download_videos_and_images.py` to measure the avg. runtim
#
COMMAND="python3 download_videos_and_images.py"
DATAFILE="perfdata/memory_baseline.txt"

# Experiment data stored as a text file in perfdata/
if [ -f $DATAFILE ]; then
    rm $DATAFILE;
fi
touch $DATAFILE
echo "Memory usage baseline expriment "$(date) >> $DATAFILE


echo "Running video download script now"
echo "COMMAND="$COMMAND
$COMMAND &
sleep 0.1

COMMANDPID=$(pgrep -f "$COMMAND")
echo "pid="$COMMANDPID

# Sample process memory usage using ps
while kill -0 $COMMANDPID;
do
    echo "taking a memory usage sample..."
    ps -p $COMMANDPID -o "rss=,vsz="  >> $DATAFILE
    sleep 1
done 

