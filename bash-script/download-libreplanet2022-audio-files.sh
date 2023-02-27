#!/bin/bash -eu

#   This is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This bash script is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   See <http://www.gnu.org/licenses/> for GNU General Public License.
#
#   contact author: brucelam1982pi@gmail.com Bruce

audio_directory=./libreplanet2022-audio
mkdir "$audio_directory"
cd "$audio_directory"
wget https://static.fsf.org/nosvn/libreplanet/2022/feed.xml
grep '<link>https://.*.ogg</link>' feed.xml | sed -e 's/ //g' -e 's/<link>//g' -e 's/<[/]link>//g' | uniq > ogg-list.txt
wget --input-file=ogg-list.txt
