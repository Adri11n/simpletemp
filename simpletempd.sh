#!/bin/bash
FILE=simpletemp.py
if [ -f "$FILE" ]; then
    ./simpletemp.py
else
    ./simpletemp
fi