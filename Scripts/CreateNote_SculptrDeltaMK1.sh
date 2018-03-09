#!/bin/bash
TIMESTAMP=$(date '+%Y.%m.%d_%H:%M:%S')
FILENAME=SculptrDeltaMK1_$TIMESTAMP.txt
touch $FILENAME
echo -e "Sculptr Delta MK1	$TIMESTAMP\n\n" > $FILENAME
gedit $FILENAME &

