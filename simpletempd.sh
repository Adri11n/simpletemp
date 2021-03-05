#!/bin/bash
FILE=simpletemp.py
if [ -f "$FILE" ]; then
    chmod +x simpletemp.py
    ./simpletemp.py
else
    chmod +x simpletemp
    ./simpletemp
fi