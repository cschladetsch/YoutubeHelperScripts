#!/bin/sh

echo "Not uploading $1 to YouTube"
echo "    If Iwas going to, I'd use upload-yt.py"

python upload-youtube.py $* 
