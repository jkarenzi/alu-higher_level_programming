#!/bin/bash
#  script that displays methods
curl -si -X "OPTIONS" $1 | grep "Allow" | cut -d " " -f 2-
