#!/bin/bash
#

newest_file=""

for file in *; do
    if [ -f "$file" ]; then
        if [ -z "$newest_file" ] || [ "$file" -nt "$newest_file" ]; then
            newest_file="$file"
        fi
    fi
done

file="`basename $newest_file`.mp4"
output="$newest_file-converted.mp4"

echo ">>>>> Converting $newest_file $output <<<<<"

convert-yoiutube.sh $newest_file $output

wq
upload-yt.st $output

start .

