#!/bin/bash
# first launch option should be the input files (e.g. /path/to/directory/*.png
# second option is the output file
convert -delay 10 -layers optimize -loop 0 $1 $2
