#!/bin/bash -eu

for file_name in *.mp4	  
do
    #echo "$file_name"
    out_name=${file_name//mp4/mp3}
    echo "$out_name"

    tmp_out_name=${file_name//mp4/aac}
    echo ffmpeg -i "$file_name"  -vn -acodec copy "$tmp_out_name"
    ffmpeg -i "$file_name"  -vn -acodec copy "$tmp_out_name"

    echo ffmpeg -i "$tmp_out_name"   -codec:a libmp3lame -qscale:a 4 "$out_name"
    ffmpeg -i "$tmp_out_name"   -codec:a libmp3lame -qscale:a 4 "$out_name"
done
